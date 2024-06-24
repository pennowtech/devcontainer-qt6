from conan import ConanFile
from conan.tools.cmake import CMake, cmake_layout
from conan.tools.files import copy
import os

class MyQmlAppConan(ConanFile):
    name = "ipc-app"
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"
    # requires = "log4cplus/2.0.5@zeiss/stable"
    generators = "CMakeToolchain", "CMakeDeps"
    exports_sources = "src/*", "qml/*", "CMakeLists.txt"

    def requirements(self):
        # self.requires("cpp-ipc/1.3.0")
        self.requires("log4cplus/2.0.5@zeiss/stable")

    def layout(self):
        cmake_layout(self)

    def generate(self):
        # super().generate()
        self._setup_dependencies()

    def _setup_dependencies(self):
        base_build_folder = os.path.join(self.build_folder, "..")
        build_folder = os.path.join(base_build_folder, "bin")
        lib_folder = os.path.join(base_build_folder, "lib")
        qml_folder = os.path.join(base_build_folder, "qml")
        plugins_folder = os.path.join(base_build_folder, "plugins")

        self.output.info(f"Build folder QT: {build_folder}")
        pass
    
        for dep in self.dependencies.values():
            self.output.info(f"SDSINGH: {str(dep), dep.package_folder}")
            if str(dep).startswith("videobase"):
                self.output.info(f"Copying QML files from {dep.package_folder} to {qml_folder}")
                copy(self, pattern="*", src=os.path.join(dep.package_folder, "qml"), dst=qml_folder)
                copy(
                    self, pattern="*", src=os.path.join(dep.package_folder, "lib"), dst=lib_folder
                )
                copy(
                    self,
                    pattern="*",
                    src=os.path.join(dep.package_folder, "plugins"),
                    dst=plugins_folder,
                )

            elif str(dep).startswith("videocommon"):
                self.output.info(f"Copying QML files from {dep.package_folder} to {qml_folder}")
                copy(
                    self, pattern="*", src=os.path.join(dep.package_folder, "lib"), dst=lib_folder
                )

            elif str(dep).startswith("videovpu"):
                self.output.info(f"Copying QML files from {dep.package_folder} to {qml_folder}")
                copy(
                    self, pattern="*", src=os.path.join(dep.package_folder, "lib"), dst=lib_folder
                )

            elif str(dep).startswith("opcuagenerator"):
                self.output.info(f"Copying QML files from {dep.package_folder} to {qml_folder}")
                copy(
                    self, pattern="*", src=os.path.join(dep.package_folder, "lib"), dst=lib_folder
                )

            elif str(dep).startswith("open62541"):
                self.output.info(f"Copying QML files from {dep.package_folder} to {qml_folder}")
                copy(
                    self, pattern="*", src=os.path.join(dep.package_folder, "lib"), dst=lib_folder
                )

            elif str(dep).startswith("videoots"):
                self.output.info(f"Copying QML files from {dep.package_folder} to {qml_folder}")
                copy(
                    self, pattern="*", src=os.path.join(dep.package_folder, "lib"), dst=lib_folder
                )        

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        copy(self, pattern="*.h", dst=os.path.join(self.package_folder, "include"), src=os.path.join(self.source_folder, "src"))
        copy(self, pattern="*.qml", dst=os.path.join(self.package_folder, "qml"), src=os.path.join(self.source_folder, "qml"))
        copy(self, pattern="*.png", dst=os.path.join(self.package_folder, "qml/resources/icons"), src=os.path.join(self.source_folder, "qml/resources/icons"))
        copy(self, pattern="luzern-videobox", dst=os.path.join(self.package_folder, "bin"), src=os.path.join(self.build_folder, ""), keep_path=False)


    def package_info(self):
        self.cpp_info.libs = ["luzern-videobox"]
        self.cpp_info.bindirs = ["bin"]
        self.cpp_info.includedirs = ["include"]
        self.cpp_info.qmldirs = ["qml"]