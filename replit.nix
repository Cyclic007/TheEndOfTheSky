{ pkgs }: {
    deps = [
      # It is unable to find output, delete comment when fixed.
        pkgs.python38Full.output
        pkgs.java8
        pkgs.adoptopenjdk-hotspot-bin-16
    ];
}