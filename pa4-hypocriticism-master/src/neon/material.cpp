#include "neon/material.hpp"
#include <glm/gtc/constants.hpp>
#include <glm/gtc/random.hpp>
#include <random>

namespace ne {

bool DiffuseLight::scatter(const ne::Ray &r_in, const ne::Intersection &hit,
                           ne::Ray &r_out) const {
  float TH = 0.5f * 3.141592f * (float)rand() / RAND_MAX;
  float PHI = 2.0f * 3.141592f * (float)rand() / RAND_MAX;
  r_out.t = std::numeric_limits<float>::max();
  r_out.dir = glm::vec3(sin(TH) * cos(PHI), sin(TH) * sin(PHI), cos(TH));
  if (hit.n.x * r_out.dir.x + hit.n.y * r_out.dir.y + hit.n.z * r_out.dir.z <
      0) {
    r_out.dir = -r_out.dir;
  }
  r_out.o = hit.p + r_out.dir * 0.0001f;
  return false;
}

glm::vec3 DiffuseLight::emitted() const {
  return color_ * intensity_;
}

glm::vec3 DiffuseLight::attenuation() const {
	return color_;
}
glm::vec3 DiffuseLight::rho(const ne::Ray &r_in, const ne::Intersection &hit,
          ne::Ray &r_out) const {
  return color_;
}

int DiffuseLight::shadow() const { 
	return 2; 
}

bool Dielectric::scatter(const ne::Ray &r_in, const ne::Intersection &hit,
                         ne::Ray &r_out) const {
  float R_H, R_V, T_H, T_V, R, T;
  float COSTH0, COSTHI;
  if (glm::dot(hit.n, r_in.dir) < 0) {
    COSTH0 = sqrt(1.0f - (1.0f - pow(glm::dot(hit.n, r_in.dir), 2)) / (IOR_ * IOR_));
    COSTHI = glm::dot(hit.n, -r_in.dir);
    R_V = (COSTHI - IOR_ * COSTH0) / (COSTHI + IOR_ * COSTH0);
    T_V = (2 * COSTHI) / (COSTHI + IOR_ * COSTH0);
    R_H = (IOR_ * COSTHI - COSTH0) / (COSTH0 + IOR_ * COSTHI);
    T_H = (2 * COSTH0) / (COSTH0 + IOR_ * COSTHI);
    R = R_V * R_V + R_H * R_H;
    T = T_V * T_V + T_H * T_H * COSTH0 / COSTHI / IOR_ * permittivity_;
  } else {
    COSTH0 = sqrt(1.0f - (1.0f - pow(glm::dot(hit.n, r_in.dir), 2)) * (IOR_ * IOR_));
    COSTHI = glm::dot(hit.n, r_in.dir);
    R_V = (IOR_ * COSTHI - COSTH0) / (IOR_ * COSTHI + COSTH0);
    T_V = (2 * IOR_ * COSTHI) / (IOR_ * COSTHI + COSTH0);
    R_H = (COSTHI - IOR_ * COSTH0) / (IOR_ * COSTH0 + COSTHI);
    T_H = (2 * IOR_ * COSTH0) / (IOR_ * COSTH0 + COSTHI);
    R = R_V * R_V + R_H * R_H;
    T = T_V * T_V + T_H * T_H * COSTH0 / COSTHI * IOR_ / permittivity_;
  }

  if ((double)rand() / RAND_MAX > R) {
  
  glm::vec3 b;
  glm::vec3 refrect;
  if (glm::dot(hit.n, r_in.dir) < 0) {
	 COSTH0 = sqrt(1.0f - (1.0f - pow(glm::dot(hit.n, r_in.dir), 2)) / (IOR_ * IOR_));
	 b = (r_in.dir + hit.n * glm::dot(hit.n, -r_in.dir)) * (1.0f / sqrt(1.0f - pow(glm::dot(hit.n, r_in.dir), 2)));
	if (sqrt(1.0f - pow(glm::dot(hit.n, r_in.dir), 2)) > 0.01f){
		refrect = sqrt(1.0f - pow(COSTH0, 2)) * b - COSTH0 * hit.n;
	} else {
		refrect = r_in.dir;
	}
  } else {
    COSTH0 = sqrt(1.0f - (1.0f - pow(glm::dot(hit.n, r_in.dir), 2)) * (IOR_ * IOR_));
    b = (r_in.dir + hit.n * glm::dot(hit.n, -r_in.dir)) * (1.0f / sqrt(1.0f - pow(glm::dot(hit.n, r_in.dir), 2)));
    if (sqrt(1.0f - pow(glm::dot(hit.n, r_in.dir), 2)) > 0.01f) {
      refrect = sqrt(1.0f - pow(COSTH0, 2)) * b + COSTH0 * hit.n;
    } else {
      refrect = r_in.dir;
    }
  }
  glm::vec3 k, u, v, w;
  r_out.t = std::numeric_limits<float>::max();
  w = glm::normalize(refrect);
  k = glm::normalize(glm::vec3(1, 1, 1));
  while (abs(glm::dot(k, w)) > 0.9f) {
    k = glm::normalize(glm::vec3((float)rand() / RAND_MAX - 0.5f,
                                 (float)rand() / RAND_MAX - 0.5f,
                                 (float)rand() / RAND_MAX - 0.5f));
  }
  u = glm::normalize(glm::cross(k, w));
  v = cross(w, u);

  int depth = 0;
  float U = opacity_ * ((float)rand() / RAND_MAX - 0.5f);
  float V = opacity_ * ((float)rand() / RAND_MAX - 0.5f);
  r_out.dir = refrect + U * u + V * v;
  while (glm::dot(r_out.dir, -hit.n) < 0 && depth < 10) {
    r_out.dir = r_out.dir + refrect;
    r_out.dir = glm::normalize(r_out.dir);
    depth++;
  }
  if (depth == 10) {
    r_out.dir = refrect;
  }
  r_out.dir = glm::normalize(r_out.dir);
  r_out.o = hit.p + r_out.dir * 0.0001f;
  return false;
  } else {
  
  glm::vec3 reflect = 2.0f * glm::dot(hit.n, -r_in.dir) * hit.n + r_in.dir;
  glm::vec3 k, u, v, w;
  r_out.t = std::numeric_limits<float>::max();
  w = glm::normalize(reflect);
  k = glm::normalize(glm::vec3(1, 1, 1));
  while (abs(glm::dot(k, w)) > 0.9f) {
    k = glm::normalize(glm::vec3((float)rand() / RAND_MAX - 0.5f,
                                 (float)rand() / RAND_MAX - 0.5f,
                                 (float)rand() / RAND_MAX - 0.5f));
  }
  u = glm::normalize(glm::cross(k, w));
  v = cross(w, u);

  int depth = 0;
  float U = opacity_ * ((float)rand() / RAND_MAX - 0.5f);
  float V = opacity_ * ((float)rand() / RAND_MAX - 0.5f);
  r_out.dir = reflect + U * u + V * v;
  while (glm::dot(r_out.dir, hit.n) < 0 && depth < 10) {
    r_out.dir = r_out.dir + reflect;
    r_out.dir = glm::normalize(r_out.dir);
    depth++;
  }
  if (depth == 10) {
    r_out.dir = reflect;
  }
  r_out.dir = glm::normalize(r_out.dir);
  r_out.o = hit.p + r_out.dir * 0.0001f;
  return false;
  }
}

glm::vec3 Dielectric::emitted() const { 
	return glm::vec3(0.0f); 
}

glm::vec3 Dielectric::attenuation() const {
	return color_;
}
glm::vec3 Dielectric::rho(const ne::Ray &r_in, const ne::Intersection &hit,
                        ne::Ray &r_out) const {
  return color_;
}
int Dielectric::shadow() const { 
	return 0; 
}


bool Lambertian::scatter(const ne::Ray &r_in, const ne::Intersection &hit,
                         ne::Ray &r_out) const {
  float TH = 0.5f * 3.141592f * (float)rand() / RAND_MAX;
  float PHI = 2.0f * 3.141592f * (float)rand() / RAND_MAX;
  r_out.t = std::numeric_limits<float>::max();
  r_out.dir = glm::vec3(sin(TH) * cos(PHI), sin(TH) * sin(PHI), cos(TH));
  if (hit.n.x * r_out.dir.x + hit.n.y * r_out.dir.y + hit.n.z * r_out.dir.z <
      0) {
    r_out.dir = -r_out.dir;
  }
  r_out.o = hit.p + r_out.dir * 0.0001f;
  return false;
}
glm::vec3 Lambertian::emitted() const {
	return glm::vec3(0.0f); 
}

glm::vec3 Lambertian::attenuation() const {
	return color_;
}
glm::vec3 Lambertian::rho(const ne::Ray &r_in, const ne::Intersection &hit,
                        ne::Ray &r_out) const {
  return color_;
}
int Lambertian::shadow() const { 
	return 1; 
}

bool Metal::scatter(const ne::Ray &r_in, const ne::Intersection &hit,
                    ne::Ray &r_out) const {
  glm::vec3 reflect = 2.0f * glm::dot(hit.n, -r_in.dir) * hit.n + r_in.dir;
  glm::vec3 k, u, v, w;
  r_out.t = std::numeric_limits<float>::max();
  w = glm::normalize(reflect);
  k = glm::normalize(glm::vec3(1, 1, 1));
  while (abs(glm::dot(k, w)) > 0.9f) {
  k = glm::normalize(glm::vec3((double)rand() / RAND_MAX - 0.5f, (double)rand() / RAND_MAX - 0.5f, (double)rand() / RAND_MAX - 0.5f));
  }
  u = glm::normalize(glm::cross(k, w));
  v = cross(w, u);

  int depth = 0;
  float U = roughness_ * ((float)rand() / RAND_MAX - 0.5f);
  float V = roughness_ * ((float)rand() / RAND_MAX - 0.5f);
  r_out.dir = reflect + U *u + V * v;
  while (glm::dot(r_out.dir, hit.n) < 0 && depth < 10) {
    r_out.dir = r_out.dir + reflect;
    r_out.dir = glm::normalize(r_out.dir);
    depth++;
  }
  if (depth == 10) {
    r_out.dir = reflect;
  }
  r_out.dir = glm::normalize(r_out.dir);
  r_out.o = hit.p + r_out.dir * 0.0001f;
  return false;
}
glm::vec3 Metal::emitted() const { 
	return glm::vec3(0.0f); 
}

glm::vec3 Metal::attenuation() const { 
	return color_;
}
glm::vec3 Metal::rho(const ne::Ray &r_in, const ne::Intersection &hit,
                        ne::Ray &r_out) const {
  glm::vec3 reflect = glm::normalize(2.0f * glm::dot(-r_in.dir, hit.n) * hit.n + r_in.dir);
  return color_;
}
int Metal::shadow() const {
	return 3; 
}
} // namespace ne
