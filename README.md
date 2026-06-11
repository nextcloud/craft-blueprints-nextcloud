<!--
  - SPDX-License-Identifier: BSD-2-Clause
  - SPDX-FileCopyrightText: 2021 Nextcloud GmbH and Nextcloud contributors
-->

# 🖥️ Nextcloud Desktop Client blueprints

:blue_book: We decided to use [KDE Craft](https://community.kde.org/Craft) to get all binary dependencies of the [Nextcloud files desktop client](https://github.com/nextcloud/desktop).

## System requirements
- Windows 10, Windows 11, macOS 13 Ventura (or newer) or Linux
- [🔽 Inkscape (to generate icons)](https://inkscape.org/release/)
- Developer tools: cmake, clang/gcc/g++:
- Qt6 since 3.14, Qt5 for earlier versions
- OpenSSL
- [🔽 QtKeychain](https://github.com/frankosterfeld/qtkeychain)
- SQLite
- [Xcode](https://developer.apple.com/xcode/) (only on macOS)

#### Optional recommendations:
- [Qt Creator IDE](https://www.qt.io/product/development-tools)
- [delta: A viewer for git and diff output](https://github.com/dandavison/delta)

> [!TIP]
> We highly recommend [Nextcloud development environment on Docker Compose](https://juliushaertl.github.io/nextcloud-docker-dev/) for testing/bug fixing/development.<br>
> ▶️ https://juliushaertl.github.io/nextcloud-docker-dev/

### How to set up Windows 11 for developemtn
If you don't have Windows as your main system, you could try to run it as a [virtual machine](https://developer.microsoft.com/en-us/windows/downloads/virtual-machines/).
  
  #### Set up Microsoft Visual Studio:
  1. Open the `Visual Studio Installer`.
  2. Click on `Modify`:
     
     ![vs-studio-2022](https://github.com/user-attachments/assets/6df5e7b9-d1e0-43a9-897e-98f4c37726a9)
  
  4. Select `Desktop development with C++`:
  
     ![vs-studio-dev](https://github.com/user-attachments/assets/6fef8b8d-d8e3-4ced-b23d-8818f9813c5f)

## Set up KDE Craft
1. You will need to install Python 3: https://www.python.org/downloads/windows/
2. Set up KDE Craft as instructed in [Setting up Craft](https://community.kde.org/Craft).
3. We recommend to use the default options, including Qt6 (since desktop 3.14, we are using Qt 6).

> [!IMPORTANT]
> `C:\CraftRoot` is the path used by default by `KDE Craft` on Windows. <br>
> On Linux and macOS, `CraftRoot` is set at the user's home: `~/CraftRoot`.
> In the instructions below we will use `<CraftRoot>` to be replaced according to your operating system and set up.

## How to use the desktop client blueprints
1. After following the instructions in [Setting up Craft](https://community.kde.org/Craft).
2. Open `PowerShell` on Windows, or any terminal in other systems.
4. Run `craftenv.ps1` as described in the instructions above:
```
<CraftRoot>\craft\craftenv.ps1
```
4. Add the blueprints from this repository:
```
craft --add-blueprint-repository https://github.com/nextcloud/desktop-client-blueprints.git
```
5. Update craft:
```
$ craft craft
```
6. Install all desktop client dependencies:
```
craft --install-deps nextcloud-client
```

## Compiling the desktop client
### Windows 
1. Make sure your environment variable `%PATH%` has no conflicting information to the environment you will use to compile the client. For instance, if you have installed `OpenSSL` previously and have added it to `%PATH%`, the `OpenSSL` installed might be a different version than what was installed via `KDE Craft`.
2. To use the tools installed with Visual Studio, you need the following in your %PATH%:
![path](https://github.com/user-attachments/assets/ce99a488-22d9-4cf5-8b55-d6ae9e683845)
3. Open the `Command Prompt` (cmd.exe).

> [!IMPORTANT]
> The next steps has only been tested and proven to work when using `Command Prompt`.

4. Run:
```
"C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvarsall.bat" x64
```
> [!TIP]
> Alternatively you can use the tools installed with `KDE Craft` by adding them to `%PATH%` in your current session:
> ```
> set "PATH=<CraftRoot>\bin;<CraftRoot>\dev-utils\bin;%PATH%"
> ```
> You also need to set the Qt path for plugins via an environment variable
> ```
> set "QT_PLUGIN_PATH=<CraftRoot>\bin\plugins"
> ```
> This will result in using the `cmake` version downloaded with `KDE Craft`.
5. Clone the desktop client repository.
```
git clone https://github.com/nextcloud/desktop.git
```
6. Create the build folder `<build-folder>`.
```
mkdir <build-folder>
```
7. Go into the build folder.
```
cd <build-folder>
```
8. Run cmake.
```
cmake <desktop-cloned-repo> -G Ninja -DCMAKE_INSTALL_PREFIX=. -DCMAKE_PREFIX_PATH=<CraftRoot> -DBUILD_TESTING=ON -DNEXTCLOUD_DEV=ON -DCMAKE_BUILD_TYPE=RelWithDebInfo
```
9. Compile the desktop client
```
cmake --build .
```

### Linux and macOS
After cloning the desktop client code:
1. Clone the desktop client repository.
```
git clone https://github.com/nextcloud/desktop.git
```
2. Create the build folder `<build-folder>`.
```
mkdir <build-folder>
```
3. Go into the build folder.
```
cd <build-folder>
```
4. Run cmake.
```
cmake <desktop-cloned-repo> -DCMAKE_INSTALL_PREFIX=. -DCMAKE_PREFIX_PATH=<CraftRoot> -DBUILD_TESTING=ON -DNEXTCLOUD_DEV=ON -DCMAKE_BUILD_TYPE=Debug
```
5. Compile the desktop client
```
make install
```

> [!TIP]
> In case of seeing this error when running `cmake`:
> ```
> The following required packages were not found:
>  - libp11
> ```
> Try the following - it should work for any missing dependency:
> 1. Verify that `libp11.pc` is actually in the `CraftRoot` folder, usually it is found at `<CraftRoot>/lib/pkgconfig`.
> 2. Check which `libp11` `cmake` is finding by running in the build folder:
>    `pkg-config --libs libp11`
> 3. If it is finding another version of `libp11` in your system instead of the `CraftRoot` one, you can either:
>    3.1 Remove the second `libp11` installed or
>    3.2 Point `cmake` to the correct one:
>    `export PKG_CONFIG_PATH=<CraftRoot>/lib/pkgconfig`

> [!NOTE]
> ❓ If you have questions about it, you may use the forums at https://help.nextcloud.com to ask them.<br>
> 🐛 If you find bugs with these steps, you may open a GH issue at https://github.com/nextcloud/desktop/issues.
