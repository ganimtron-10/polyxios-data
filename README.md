# polyxios-data

Test data for [polyxios](https://github.com/fury-gl/polyxios) codec integration testing.

---

## Releases

<!-- UNRELEASED_RELEASE_START -->
### Latest Release

### Release Details

| Format Release | Format | Files | Size |
|----------------|--------|-------|------|
| `abaqus` | ABAQUS | 5 | 14.6 KB |
| `gmsh` | GMSH | 2 | 10.8 KB |
| `obj` | OBJ | 34 | 112.0 MB |

### Model Names Catalog
<details>
<summary><b>Show all models...</b></summary>

- **abaqus**: `UUea.inp`, `beam-buckl_calculix.inp`, `element_elset.inp`, `nle1xf3c.inp`, `timber_modal_calculix.inp`
- **gmsh**: `insulated-2.2.msh`, `insulated-4.1.msh`
- **obj**: `alligator.obj`, `armadillo.obj`, `ateneam.obj`, `beast.obj`, `beetle-alt.obj`, `beetle.obj`, `bimba.obj`, `cheburashka.obj`, `cow.obj`, `elepham.obj`, `elephav.obj`, `fandisk.obj`, `happy.obj`, `homer.obj`, `horse.obj`, `igea.obj`, `lucy.obj`, `max-planck.obj`, `mba1.obj`, `mba2.obj`, `mni-surface-mesh.obj`, `nefertiti.obj`, `ogre.obj`, `rocker-arm.obj`, `spot.obj`, `stanford-bunny.obj`, `star-wars-vader-tie-fighter.obj`, `suzanne.obj`, `teapot.obj`, `tree.obj`, `utah_teapot.obj`, `venusm.obj`, `woody.obj`, `xyzrgb_dragon.obj`

</details>
<!-- UNRELEASED_RELEASE_END -->

---

## Attribution & Disclaimer

Assets are curated from public-domain files, academic benchmark sets, and open-source
repositories. They are used **strictly for testing, parser compliance validation, and
performance benchmarking**. All files remain the intellectual property of their respective
authors. If you are the copyright holder of any asset and wish it removed, please open an issue.

Sources used in v0.2.0:

| Repository | License |
|-----------|---------|
| [nschloe/meshio](https://github.com/nschloe/meshio) | MIT |
| [mikedh/trimesh](https://github.com/mikedh/trimesh) | MIT |
| [MmgTools/Mmg](https://github.com/MmgTools/Mmg) | LGPL-3.0 |
| [RBniCS/RBniCS](https://github.com/RBniCS/RBniCS) | LGPL-3.0 |
| [libigl/libigl-tutorial-data](https://github.com/libigl/libigl-tutorial-data) | MPL-2.0 |
| [KratosMultiphysics/Kratos](https://github.com/KratosMultiphysics/Kratos) | BSD (4-clause) |
| [lanl/LaGriT](https://github.com/lanl/LaGriT) | BSD (LA-CC-15-069) |
| [calculix/ccx_prool](https://github.com/calculix/ccx_prool) | GPL-2.0 |

---

## Usage

### CLI Usage

The `pxios` CLI tool can be used to list and fetch available models:

```bash
pxios list                 # list all models present
pxios fetch model.ext      # fetch a specific model
pxios fetch ext            # fetch all models of an extension
```

### Fetch via Python

```python
from polyxios.fetcher import fetch, fetch_by_extension

# Fetch a single file - downloads the format archive on first use
path = fetch("cube86.mesh")         # medit format
path = fetch("pyra_cube.ugrid")     # ugrid format
path = fetch("20mm-xyz-cube.stl")   # stl format

# Fetch all files of a format
paths = fetch_by_extension(".inp")  # all abaqus test files
```

Data is cached in `~/.polyxios/` (override with `POLYXIOS_HOME` env var).

### Direct download via curl / wget

```bash
# Format: https://github.com/fury-gl/polyxios-data/releases/download/<tag>/<format>.zip

curl -LO https://github.com/fury-gl/polyxios-data/releases/download/v0.2.0/medit.zip
curl -LO https://github.com/fury-gl/polyxios-data/releases/download/v0.1.0/ply.zip
```
