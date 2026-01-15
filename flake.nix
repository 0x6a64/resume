{
  description = "Astro development environment for Resume";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = {
    self,
    nixpkgs,
    flake-utils,
  }:
    flake-utils.lib.eachDefaultSystem (
      system: let
        pkgs = nixpkgs.legacyPackages.${system};
      in {
        devShells.default = pkgs.mkShell {
          name = "astro-dev";

          buildInputs = [
            # Node.js runtime
            pkgs.nodejs_22

            # Package managers
            pkgs.nodePackages.pnpm

            # Required for sharp (Astro image optimization)
            pkgs.vips
            pkgs.pkg-config

            # Required for node-gyp (native module compilation)
            pkgs.python3

            # Development tools
            pkgs.nodePackages.typescript
            pkgs.nodePackages.typescript-language-server

            # Nix development tools
            pkgs.alejandra  # Nix formatter (for .nixd.json)

            # Optional: Uncomment as needed
            # pkgs.nodePackages.prettier # Code formatter
          ];

          shellHook = ''
            echo "Astro development environment loaded"
            echo "Node.js version: $(node --version)"
            echo "pnpm version: $(pnpm --version)"

            # Set up pnpm to use local node_modules/.bin
            export PATH="$PWD/node_modules/.bin:$PATH"

            # Install dependencies if package.json exists and node_modules doesn't
            if [ -f package.json ] && [ ! -d node_modules ]; then
              echo ""
              echo "Installing dependencies..."
              pnpm install
            fi

            echo ""
            echo "Commands available:"
            echo "  pnpm dev     - Start development server"
            echo "  pnpm build   - Build for production"
            echo "  pnpm preview - Preview production build"
          '';
        };
      }
    );
}
