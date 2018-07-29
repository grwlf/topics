# This file contains definition of work environment for Nix-systems
# See also http://www.nixos.org/nix
# Use `nix-shell` command to activate the environment

{ pkgs ?  import <nixpkgs> {}
, stdenv ? pkgs.stdenv
} :
let

  self = pkgs.python36Packages;
  inherit (self) buildPythonPackage fetchPypi;

  shell = stdenv.mkDerivation {
    name = "buildenv";
    buildInputs =
      with pkgs;
      with self;
    [
      universal-ctags
      python
      ipython
      numpy
      matplotlib
      git
      jupyter_console
      jupyter
      nbformat
      scipy
      pyqt5
      pandas
      scikitlearn
      seaborn
      graphviz
      tqdm
      joblib
      cmake
    ];

    shellHook = with pkgs; ''
      if test -f /etc/myprofile ; then
        . /etc/myprofile
      fi

      mkdir .ipython-profile 2>/dev/null || true
      cat >.ipython-profile/ipython_config.py <<EOF
      print("Enabling autoreload")
      c = get_config()
      c.InteractiveShellApp.exec_lines = []
      c.InteractiveShellApp.exec_lines.append('%load_ext autoreload')
      c.InteractiveShellApp.exec_lines.append('%autoreload 2')
      EOF

      export CWD=`pwd`
      export PYTHONPATH="$CWD/src:$PYTHONPATH"
      export MPLBACKEND='Qt5Agg'
      alias ipython='ipython --matplotlib=qt5  --profile-dir=.ipython-profile'
    '';
  };

in
  shell

