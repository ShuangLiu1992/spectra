from conan import ConanFile
import conan.tools.files
from conan.tools.cmake import CMake, cmake_layout
import os


class SPECTRAConan(ConanFile):
    name = "spectra"
    settings = "os", "build_type", "compiler", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    generators = "CMakeDeps", "CMakeToolchain"

    def requirements(self):
        self.requires(f"eigen/{self.version}")

    def export_sources(self):
        conan.tools.files.copy(self, "*", self.recipe_folder, self.export_sources_folder)

    def layout(self):
        cmake_layout(self)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.install()

    def package_info(self):
        self.cpp_info.set_property("cmake_find_mode", "none")
        self.cpp_info.builddirs.append(os.path.join("share", "spectra", "cmake"))
