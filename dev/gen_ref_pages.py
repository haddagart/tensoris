"""Automatically generate API reference pages for all Python modules in src/.

Enforces custom navigation ordering at every tree level:
1. Modules (files) always appear BEFORE packages (directories).
2. All items within modules and packages are sorted in alphabetical order.
"""

from pathlib import Path
import mkdocs_gen_files

# Human-readable title mapping for packages and modules in navigation tree
NAV_TITLES = {
    "backend": "Backend Engine",
    "components": "Components",
    "blocks": "Neural Blocks",
    "layers": "Atomic Layers",
    "losses": "Loss Functions",
    "metrics": "Evaluation Metrics",
    "trainers": "Trainers",
    "data": "Data Management",
    "lib": "Utilities & Helpers",
    "models": "Model Architectures",
    "cv": "Computer Vision",
    "nlp": "Natural Language Processing",
    "genai": "Generative AI",
    "trainer": "Model Trainer",
    "dataset": "Base Dataset",
    "utils": "Core Utilities",
    "backbone": "ResNet Backbone",
    "transformer": "Transformer Classifier",
    "vae": "Variational Autoencoder",
    "model": "Base Model",
    "integrations": "Integrations",
    "huggingface": "Hugging Face",
    "kaggle": "Kaggle",
    "roboflow": "Roboflow",
    "ultralytics": "Ultralytics YOLO",
    "wandb": "Weights & Biases",
}


class NavNode:
    """Tree node representing a directory/package or root in navigation tree."""

    def __init__(self, title: str):
        self.title = title
        self.modules: dict[str, str] = {}  # title -> doc_path
        self.packages: dict[str, NavNode] = {}  # title -> NavNode


src_dir = Path("src")
root = NavNode("API Reference")

for path in sorted(src_dir.rglob("*.py")):
    module_path = path.relative_to(src_dir).with_suffix("")
    parts = tuple(module_path.parts)

    # Skip __init__.py and __main__.py so folder headers display child modules directly
    if not parts or parts[-1] in ("__init__", "__main__"):
        continue

    doc_path = path.relative_to(src_dir).with_suffix(".md")
    full_doc_path = Path("api", doc_path)

    # Generate virtual Markdown API doc file for mkdocstrings parsing
    with mkdocs_gen_files.open(full_doc_path, "w") as fd:
        identifier = ".".join(parts)
        fd.write(f"::: {identifier}\n")

    mkdocs_gen_files.set_edit_path(full_doc_path, path)

    # Populate navigation tree hierarchy
    current = root
    for part in parts[:-1]:
        title = NAV_TITLES.get(part, part.replace("_", " ").title())
        if title not in current.packages:
            current.packages[title] = NavNode(title)
        current = current.packages[title]

    leaf_part = parts[-1]
    leaf_title = NAV_TITLES.get(leaf_part, leaf_part.replace("_", " ").title())
    current.modules[leaf_title] = doc_path.as_posix()


def render_nav_tree(node: NavNode, indent: int = 0) -> list[str]:
    """Recursively render literate navigation tree with modules before packages."""
    lines = []
    prefix = "    " * indent

    # 1. Render modules (files) first, sorted alphabetically by title
    for title in sorted(node.modules.keys()):
        doc_path = node.modules[title]
        lines.append(f"{prefix}* [{title}]({doc_path})\n")

    # 2. Render subpackages (directories) second, sorted alphabetically by title
    for title in sorted(node.packages.keys()):
        lines.append(f"{prefix}* {title}\n")
        lines.extend(render_nav_tree(node.packages[title], indent + 1))

    return lines


# Write custom ordered SUMMARY.md for mkdocs-literate-nav
with mkdocs_gen_files.open("api/SUMMARY.md", "w") as nav_file:
    nav_file.writelines(render_nav_tree(root))
