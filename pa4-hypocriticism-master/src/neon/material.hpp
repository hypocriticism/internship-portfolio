#ifndef __MATERIAL_H_
#define __MATERIAL_H_

#include "neon/blueprint.hpp"
#include "neon/intersection.hpp"
#include "neon/ray.hpp"

namespace ne {

namespace abstract {

// Absract material class for inteface
// you can add/change variables/methods if you want
class Material {
public:
  virtual bool scatter(const ne::Ray &r_in, const ne::Intersection &hit,
                       ne::Ray &r_out) const = 0;

  virtual glm::vec3 emitted() const { return glm::vec3(0.0f); }

  virtual glm::vec3 attenuation() const = 0;

  virtual glm::vec3 rho(const ne::Ray &r_in, const ne::Intersection &hit,
                    ne::Ray &r_out) const = 0;
  virtual int shadow() const = 0;

protected:
};

} // namespace abstract

/*  Actual implementation of materials  */
// you can add/change variables/methods if you want

// Light material which glow unifomly.
class DiffuseLight final : public ne::abstract::Material {
public:
  DiffuseLight(const glm::vec3 &color = glm::vec3(1.0), float intensity = 0.0f) : color_(color), intensity_(intensity){}

  bool scatter(const ne::Ray &r_in, const ne::Intersection &hit,
               ne::Ray &r_out) const override;

  glm::vec3 emitted() const override;

  glm::vec3 attenuation() const override;
  glm::vec3 rho(const ne::Ray &r_in, const ne::Intersection &hit,
            ne::Ray &r_out) const override;
  int shadow() const override;

private:
  glm::vec3 color_;
  float intensity_;
};

// material which obeys Fresnel's equation
// 
class Dielectric final : public ne::abstract::Material {
public:
  Dielectric(const glm::vec3 &color = glm::vec3(0.7f), float IOR = 0.7f, float opacity = 0.0f, float permittivity = 1.0f)
      : color_(color), IOR_(IOR) , opacity_(opacity), permittivity_(permittivity){}

  bool scatter(const ne::Ray &r_in, const ne::Intersection &hit,
               ne::Ray &r_out) const override;

  glm::vec3 emitted() const override;

  glm::vec3 attenuation() const override;
  glm::vec3 rho(const ne::Ray &r_in, const ne::Intersection &hit,
            ne::Ray &r_out) const override;
  int shadow() const override;

protected:
  glm::vec3 color_{1.0, 1.0, 1.0};
  float IOR_ = 0.5f;
  float opacity_ = 0.0f;
  float permittivity_ = 1.0f;
};

// material which reflect ray toward random direction
class Lambertian final : public ne::abstract::Material {
public:
  Lambertian(const glm::vec3 color = glm::vec3{0.f, 0.f, 0.f})
      : color_(color) {}

  bool scatter(const ne::Ray &r_in, const ne::Intersection &hit,
               ne::Ray &r_out) const override;

  glm::vec3 emitted() const override;

  glm::vec3 attenuation() const override;
  glm::vec3 rho(const ne::Ray &r_in, const ne::Intersection &hit,
            ne::Ray &r_out) const override;
  int shadow() const override;

protected:
  glm::vec3 color_{0.7f, 0.7f, 0.7f};
};

// metal obeys law of reflection
class Metal final : public ne::abstract::Material {
public:
  Metal(const glm::vec3 color = glm::vec3{0.0f, 0.0f, 0.f}, float blurr = 0.2f)
      : color_(color), roughness_(glm::clamp(blurr, 0.0f, 1.0f)) {}

  bool scatter(const ne::Ray &r_in, const ne::Intersection &hit,
               ne::Ray &r_out) const override;

  glm::vec3 emitted() const override;

  glm::vec3 attenuation() const override;
  glm::vec3 rho(const ne::Ray &r_in, const ne::Intersection &hit,
            ne::Ray &r_out) const override;
  int shadow() const override;

protected:
  glm::vec3 color_{0.9f, 0.9f, 0.9f};
  float roughness_ = 0.0f;
};

} // namespace ne

#endif // __MATERIAL_H_
