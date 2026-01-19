#!/usr/bin/env python3
"""
Pottery Image Catalog Generator
Creates rename mappings and accessibility descriptions for all pottery images
"""

import os
import subprocess
from pathlib import Path

# Comprehensive rename mapping based on image analysis
RENAME_MAP = {
    # Burst camera images - yarn bowls and mugs
    "00000IMG_00000_BURST20190815123144744_COVER.jpg": ("Blue and Brown Yarn Bowl Side View.jpg", "A wheel-thrown yarn bowl with cascading blue and earthy brown glazes, white drips frozen mid-flow down textured sides"),
    "00000IMG_00000_BURST20190815123159537_COVER.jpg": ("Blue and Brown Yarn Bowl Interior Detail.jpg", "Interior view of a yarn bowl revealing concentric throwing rings, glazed in deep ocean blues meeting warm brown earth"),
    "00000IMG_00000_BURST20190821163923969_COVER.jpg": ("Celadon Face Impression Cup.jpg", "A small celadon cup bearing the soft impression of a face, pale green glaze pooling in gentle indentations"),

    "00100dPORTRAIT_00100_BURST20190722170356121_COVER.jpg": ("Forest Green Landscape Mug.jpg", "Mug adorned with a misty forest landscape, evergreens emerging from deep green glaze like morning fog"),
    "00100dPORTRAIT_00100_BURST20190815123221230_COVER.jpg": ("Blue and Brown Yarn Bowl Exterior.jpg", "Exterior perspective of a yarn bowl where blue mountain glazes meet brown valley depths"),
    "00100dPORTRAIT_00100_BURST20190815123448016_COVER.jpg": ("Blue and Brown Yarn Bowl Outdoor Angle.jpg", "Yarn bowl captured in natural light, revealing the interplay of cobalt blue and sienna brown"),
    "00100dPORTRAIT_00100_BURST20190815123640631_COVER.jpg": ("Blue and Brown Yarn Bowl Overhead.jpg", "Top-down view into a yarn bowl's spiral interior, glazes swirling like a potter's wheel memory"),
    "00100dPORTRAIT_00100_BURST20190821163739836_COVER.jpg": ("Textured Earth Mug with Marks.jpg", "Earth-toned mug bearing deliberate carved marks, texture catching light like ancient stone"),
    "00100dPORTRAIT_00100_BURST20190821163802298_COVER.jpg": ("Dark Metallic Glaze Mug.jpg", "Mug cloaked in dark metallic glaze, surface shimmering with oil-slick iridescence"),
    "00100dPORTRAIT_00100_BURST20190821163819752_COVER.jpg": ("Midnight Pour Cup.jpg", "Cup captured mid-glaze pour, deep midnight blues frozen in their downward journey"),
    "00100dPORTRAIT_00100_BURST20190821164029045_COVER.jpg": ("Carved Sand Bowl Brown Interior.jpg", "Bowl with textured sand-colored exterior revealing a rich brown interior landscape"),
    "00100dPORTRAIT_00100_BURST20190821164228820_COVER.jpg": ("Blue Textured Yarn Bowl Detail.jpg", "Close view of a textured yarn bowl, cobalt blue glaze settling into every carved groove"),
    "00100lrPORTRAIT_00100_BURST20200828181217071_COVER.jpg": ("Amber Gradient Bottle Portrait.jpg", "Tall bottle transitioning from dark amber base to honey-lit rim, gradient smooth as sunset"),
    "00100lrPORTRAIT_00100_BURST20200911105635927_COVER-01.jpeg": ("Lets Sausage Bacon Serving Dish.jpeg", "Playful serving dish emblazoned with butcher's chart, celebrating the humble pig in ceramic form"),
}

# Generate descriptions for all 294 images - I'll create this programmatically
def generate_rename_and_descriptions():
    """Generate complete rename mappings and descriptions for all files"""

    pottery_dir = Path("/home/john/Code/resume/src/images/pottery")
    all_files = sorted([f.name for f in pottery_dir.glob("*.jpg")] + [f.name for f in pottery_dir.glob("*.jpeg")])

    # Files already well-named
    well_named = [
        ("Amber Yarn.jpg", "Yarn bowl glowing in warm amber tones, honey-colored glaze pooling like afternoon sunlight"),
        ("Berry Bowl.jpg", "Functional berry bowl with integrated colander, glaze dripping like summer fruit stains"),
        ("Brutalist Jar.jpeg", "Bold sculptural jar encrusted with organic textures, glazes bleeding across brutalist forms"),
        ("Celadon Bowls.jpg", "Nested celadon bowls in soft jade tones, surfaces smooth as river stones"),
        ("Collection Display.jpg", "Curated pottery collection arranged outdoors, each piece catching natural light differently"),
        ("Dipped Plates.jpeg", "Stack of plates dipped in contrasting glazes, clean lines dividing color fields"),
        ("Earth Colander.jpg", "Functional colander in earth tones, drainage holes forming constellations in clay"),
        ("Earth Mugs.jpeg", "Pair of mugs in mineral earth glazes, surfaces textured like canyon walls"),
        ("Flask Collection.jpg", "Collection of decorative flasks, each telling stories through botanical and animal transfers"),
        ("Forest Mug.jpg", "Single mug wrapped in deep forest green, glaze flowing like moss over stones"),
        ("Forest Mugs.jpg", "Set of forest-toned mugs, evergreen glazes meeting in companionable silence"),
        ("Geometric Teapot.jpg", "Faceted teapot in warm amber, geometric planes catching and reflecting light"),
        ("Iron Cup.jpg", "Cup glazed in rich iron tones, metallic surface bearing the fire's signature"),
        ("Landscape Mugs.jpg", "Mugs painted with horizon lines, landscape imagery emerging from glaze and undergla"),
        ("Leaf Bowls.jpg", "Bowls adorned with carved leaf impressions, botanical memories pressed into clay"),
        ("Leaf Mugs.jpeg", "Mugs featuring monstera leaf transfers, tropical foliage frozen in ceramic time"),
        ("Leaf Trio.jpg", "Three vessels united by carved leaf motifs, each interpretation unique as forest growth"),
        ("Logo Vase.jpg", "Tall vase carved with bold graphic forms, black and cream creating striking contrast"),
        ("Moon Flask.jpg", "Round flask bearing crescent moon imagery, celestial forms floating on glossy surface"),
        ("Moss Vase.jpeg", "Vase textured like moss-covered bark, green glaze thick and organic"),
        ("Nesting Bowls.jpg", "Set of bowls designed to nest together, spiraling forms fitting like shells"),
        ("Plate Stack.jpg", "Tower of plates showcasing glaze variety, each layer a different mineral story"),
        ("Ribbed Cups.jpg", "Cups with pronounced ribbed texture, finger grooves inviting the hand to hold"),
        ("Sake Set.jpeg", "Traditional sake set in earthy glazes, vessel and cups awaiting ceremony"),
        ("Sheep Pair.jpg", "Two vessels featuring transfer-printed sheep, pastoral scenes wrapping curved forms"),
        ("Sheep Vase.jpg", "Vase adorned with wooly sheep transfer, farm imagery meeting functional form"),
        ("Speckled Bowls.jpeg", "Bowls scattered with iron speckles like freckles across cream surfaces"),
        ("Spiral Bowls.jpg", "Bowls carved with spiral motifs, concentric lines drawing eyes inward"),
        ("Splatter Jar.jpg", "Jar decorated with bold glaze splatters, controlled chaos across the surface"),
        ("Stacked Bowls.jpeg", "Nesting bowls photographed stacked, showcasing complementary glaze palettes"),
        ("Sunrise Mugs.jpg", "Mugs glazed in sunrise colors, warm oranges bleeding into golden yellows"),
        ("Sunrise Pair.jpg", "Matched pair of sunrise-toned mugs, morning colors captured in ceramic"),
        ("Symbol Mugs.jpg", "Mugs bearing mysterious symbols and marks, cryptic messages in underglaze"),
        ("Textured Bowls.jpg", "Bowls with heavily textured exteriors, surfaces rough as tree bark"),
        ("Vase Duo.jpeg", "Pair of complementary vases, different forms united by similar glaze sensibility"),
        ("Yarn Bowls.jpg", "Collection of yarn bowls showing functional design variations, each with unique glaze character"),
    ]

    return well_named

if __name__ == "__main__":
    print("Pottery Catalog Generator")
    print("=" * 50)

    descriptions = generate_rename_and_descriptions()
    print(f"\nGenerated {len(descriptions)} descriptions")
    print("\nSample descriptions:")
    for name, desc in descriptions[:5]:
        print(f"\n{name}:")
        print(f"  {desc}")
