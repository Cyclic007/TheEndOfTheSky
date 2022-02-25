{ pkgs }: {
    deps = [
        pkgs.python38Full.outpipp
        pkgs.java8
        pkgs.adoptopenjdk-hotspot-bin-16
    ];
}