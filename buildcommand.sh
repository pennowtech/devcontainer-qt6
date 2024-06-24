cd .. && rm -rf build && conan install . --profile:build conan-debug-profile --profile:host conan-debug-profile --build=missing && cd build && cmake .. -DCMAKE_BUILD_TYPE=Debug && make
