#include "integrator.hpp"
#include "neon/intersection.hpp"
#include "neon/material.hpp"
#include "neon/scene.hpp"

namespace ne {

namespace core {

	// unused
glm::vec3 Integrator::integrate(const ne::Ray &ray,
                                std::shared_ptr<ne::Scene> scene) {
  glm::vec3 L{0.0f};

  return L;
}

} // namespace core
} // namespace ne
