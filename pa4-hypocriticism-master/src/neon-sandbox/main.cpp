#include "test.hpp"

#include "neon/camera.hpp"
#include "neon/image.hpp"
#include "neon/integrator.hpp"
#include "neon/material.hpp"
#include "neon/ray.hpp"
#include "neon/scene.hpp"
#include "neon/sphere.hpp"
#include "neon/utils.hpp"

#include <glm/gtx/string_cast.hpp>
#include <iostream>
#include <memory>
#include <taskflow/taskflow.hpp>

glm::vec3 scatter(const ne::Ray &r_in, std::shared_ptr<ne::Scene> scene, float scaatter_coef);
int main(int argc, char *argv[]) {
  // number of pixel
  int nx = 512;
  int ny = 512;

  // create output image
  ne::Image canvas(nx, ny);

  // create scene
  std::shared_ptr<ne::Scene> scene = testScene1();

  // spwan camera
  static ne::Camera camera;
  float distToFocus = 4;
  float aperture = 0.0f;
  //glm::vec3 lookfrom(0, 2, 3);
  glm::vec3 lookfrom(0, 0, 3);
  glm::vec3 lookat(0, 0, 0);
  //glm::vec3 light(0.1f, 0.1f, 0.1f);
  glm::vec3 light(0.5f, 0.5f, 0.9f);
  camera = ne::Camera(lookfrom, lookat, glm::vec3(0, 1, 0), 60,
                      float(canvas.width()) / float(canvas.height()), aperture,
                      distToFocus);

  // summon progress bar. this is just eye candy.
  // you can use timer class instead
  ne::utils::Progressbar progressbar(canvas.numPixels());

  // variables
  ne::Ray rout1, rout2, s;
  ne::Intersection rout_hit, s_hit;
  ne::Lambertian Lamb;
  int spp = 128;
  int depth;
  glm::vec3 temp;
  float cosine;

  progressbar.start();

  // pixel loop
  for (unsigned int m = 0; m < canvas.width(); m++) {
    for (unsigned int n = 0; n < canvas.height(); n++) {

	// initialize color
      glm::vec3 color{0.0f};

	  // antialising loop
      for (int t = 0; t < spp; t++) {
        for (int i = 0; i < 4; i++) {
          float u = float(m + 0.5f * ((i % 2) - 0.5f)) / float(canvas.width());
          float v = float(n + 0.5f * ((i / 2) - 0.5f)) / float(canvas.height());
          u += 0.5f * ((float)rand() / RAND_MAX - 0.5f) / float(canvas.width());
          v += 0.5f * ((float)rand() / RAND_MAX - 0.5f) / float(canvas.height());

		  // primary ray
          rout1 = camera.sample(u, v);

		  // initialize color factor
          temp = glm::vec3(1.0f);

          if (scene->rayIntersect(rout1, rout_hit) && (rout_hit.material->shadow() == 1 || rout_hit.material->shadow() == 3)) {

			// background light shadow
            Lamb.scatter(rout1, rout_hit, s);
            if (scene->rayIntersect(s, s_hit) && (s_hit.material->shadow() == 1 || s_hit.material->shadow() == 3)) {
              temp *= 1.0f - glm::dot(s.dir, rout_hit.n);
            }

			// direct light sampling
			s.t = std::numeric_limits<float>::max();
            s.dir = scene->sampleDirectLight(rout_hit);
			s.o = rout_hit.p + s.dir * 0.00001f;
            if (rout_hit.material->shadow() == 1 && scene->rayIntersect(s, s_hit) && s_hit.material->shadow() == 2) {
                          temp *= 1.0f + 
                              rout_hit.material->attenuation() *
                              s_hit.material->emitted() *
                              glm::dot(s.dir, rout_hit.n) *
                              (1.0f / (glm::dot(s.o - s_hit.p, s.o - s_hit.p) + 1.0f));
            }
          }

		  // wavelength independent Rayleigh scattering
          color += scatter(rout1, scene, 0.02f) * 0.25f;
          
		  // energy of reflected light
		  cosine = 1.0f;
		  
		  // multiple light bounce
		  depth = 0;
          while (depth < 10) {
            if (scene->rayIntersect(rout1, rout_hit)) {
              rout_hit.material->scatter(rout1, rout_hit, rout2);
              if (rout_hit.material->shadow() != 2) {
                temp *= rout_hit.material->attenuation();
              }

			  // adding emissive light
              color += temp * rout_hit.material->emitted() * cosine * 0.25f;

			  // update cosine variable
              if (glm::dot(rout2.dir, rout_hit.n) > 0 &&
                  rout_hit.material->shadow() != 0) {
                cosine *= glm::dot(rout2.dir, rout_hit.n);
              }

			  // recursive ray tracing
              rout1 = rout2;
            } else { 
              break;
            }
            depth++;
          }

		  // factoring background light
          temp *= scene->sampleBackgroundLight(rout1.dir, light);

		  // add up color
          color += temp * 0.25f;
        }
		// clamping
        color = glm::clamp(color, 0.0f, float(spp));
      }

      // record to canvas, averaging color values sampled per pixel
      canvas(m, canvas.height() - n - 1) +=
          glm::u8vec4(color * 255.99f / float(spp), 255.0f);

      // update progressbar and draw it every 10 progress
      if (++progressbar % 20 == 0)
        progressbar.display();
    }
  }
  progressbar.end();
  canvas.save("result.png");
  return 0;
}

// wavelength independent Rayleigh scattering
glm::vec3 scatter(const ne::Ray &r_in, std::shared_ptr<ne::Scene> scene, float scatter_coef) {
  ne::Ray s, r;
  ne::Intersection s_hit;
  ne::Intersection hit;
  float TH;
  float PHI;
  float pos;
  r = r_in;
  glm::vec3 sum;
  
  sum = glm::vec3{0.0f};
  pos = 3.0f;
  if(scene->rayIntersect(r, hit)){
	  while (pos < sqrt(glm::dot(hit.p - r_in.o, hit.p - r_in.o))) {
		TH = 3.141592f * (float)rand() / RAND_MAX;
		PHI = 2.0f * 3.141592f * (float)rand() / RAND_MAX;
		s.t = std::numeric_limits<float>::max();
		s.o = r_in.o + r_in.dir * pos;
		s.dir = glm::vec3(sin(TH) * cos(PHI), sin(TH) * sin(PHI), cos(TH));
		if (scene->rayIntersect(s, s_hit) && s_hit.material->shadow() == 2) {
                  sum += s_hit.material->emitted() * scatter_coef *
                         (1.0f + pow(glm::dot(r_in.dir, s.dir), 2)) *
                         (1.0f / (glm::dot(s.o - s_hit.p, s.o - s_hit.p) + 1.0f));
		}
		pos += 0.2f;
	  }
  }else{
    while (pos < 5.0f){
      TH = 3.141592f * (float)rand() / RAND_MAX;
      PHI = 2.0f * 3.141592f * (float)rand() / RAND_MAX;
      s.t = std::numeric_limits<float>::max();
      s.o = r_in.o + r_in.dir * pos;
      s.dir = glm::vec3(sin(TH) * cos(PHI), sin(TH) * sin(PHI), cos(TH));
      if (scene->rayIntersect(s, s_hit) && s_hit.material->shadow() == 2) {
        sum += s_hit.material->emitted() * scatter_coef *
               (1.0f + pow(glm::dot(r_in.dir, s.dir), 2)) *
               (1.0f / (glm::dot(s.o - s_hit.p, s.o - s_hit.p) + 1.0f));
      }
      pos += 0.2f;
	}
	}
  return sum;
}