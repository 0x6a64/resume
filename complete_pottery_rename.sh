#!/bin/bash
# Complete Pottery Image Rename Script
# Renames all 294 pottery images with descriptive names

cd /home/john/Code/resume/src/images/pottery || exit 1

echo "Starting pottery image renaming..."

# Yarn bowl series - blue and brown with white drips
git mv "00000IMG_00000_BURST20190815123144744_COVER.jpg" "Blue and Brown Yarn Bowl Side View.jpg" 2>/dev/null || echo "Already renamed or not found: Blue and Brown Yarn Bowl Side View.jpg"
git mv "00000IMG_00000_BURST20190815123159537_COVER.jpg" "Blue and Brown Yarn Bowl Interior.jpg" 2>/dev/null || echo "Already renamed or not found: Blue and Brown Yarn Bowl Interior.jpg"
git mv "00000IMG_00000_BURST20190821163923969_COVER.jpg" "Celadon Face Impression Cup.jpg" 2>/dev/null || echo "Already renamed or not found: Celadon Face Impression Cup.jpg"

# Portrait series mugs and bowls
git mv "00100dPORTRAIT_00100_BURST20190722170356121_COVER.jpg" "Forest Green Landscape Mug.jpg" 2>/dev/null || echo "Already renamed or not found: Forest Green Landscape Mug.jpg"
git mv "00100dPORTRAIT_00100_BURST20190815123221230_COVER.jpg" "Blue and Brown Yarn Bowl Outdoor View.jpg" 2>/dev/null || echo "Already renamed or not found: Blue and Brown Yarn Bowl Outdoor View.jpg"
git mv "00100dPORTRAIT_00100_BURST20190815123448016_COVER.jpg" "Blue and Brown Yarn Bowl Outdoor Angle.jpg" 2>/dev/null || echo "Already renamed or not found: Blue and Brown Yarn Bowl Outdoor Angle.jpg"
git mv "00100dPORTRAIT_00100_BURST20190815123640631_COVER.jpg" "Blue and Brown Yarn Bowl Top View.jpg" 2>/dev/null || echo "Already renamed or not found: Blue and Brown Yarn Bowl Top View.jpg"
git mv "00100dPORTRAIT_00100_BURST20190821163739836_COVER.jpg" "Textured Earth Mug with Carved Marks.jpg" 2>/dev/null || echo "Already renamed or not found: Textured Earth Mug with Carved Marks.jpg"
git mv "00100dPORTRAIT_00100_BURST20190821163802298_COVER.jpg" "Dark Metallic Mug.jpg" 2>/dev/null || echo "Already renamed or not found: Dark Metallic Mug.jpg"
git mv "00100dPORTRAIT_00100_BURST20190821163819752_COVER.jpg" "Midnight Pour Cup.jpg" 2>/dev/null || echo "Already renamed or not found: Midnight Pour Cup.jpg"
git mv "00100dPORTRAIT_00100_BURST20190821164029045_COVER.jpg" "Carved Sand Bowl with Brown Interior.jpg" 2>/dev/null || echo "Already renamed or not found: Carved Sand Bowl with Brown Interior.jpg"
git mv "00100dPORTRAIT_00100_BURST20190821164228820_COVER.jpg" "Blue Textured Yarn Bowl.jpg" 2>/dev/null || echo "Already renamed or not found: Blue Textured Yarn Bowl.jpg"
git mv "00100lrPORTRAIT_00100_BURST20200828181217071_COVER.jpg" "Amber Gradient Bottle.jpg" 2>/dev/null || echo "Already renamed or not found: Amber Gradient Bottle.jpg"
git mv "00100lrPORTRAIT_00100_BURST20200911105635927_COVER-01.jpeg" "Lets Sausage Bacon Dish.jpeg" 2>/dev/null || echo "Already renamed or not found: Lets Sausage Bacon Dish.jpeg"

# Gallery and display images
git mv "IMG_20190405_164602.jpg" "Teal and Burgundy Gallery Vase.jpg" 2>/dev/null || echo "Already renamed or not found: Teal and Burgundy Gallery Vase.jpg"
git mv "IMG_20190612_155650.jpg" "Three Spiral Bowls Outdoor Display.jpg" 2>/dev/null || echo "Already renamed or not found: Three Spiral Bowls Outdoor Display.jpg"
git mv "IMG_20190612_155733.jpg" "Celadon Lidded Jar and Bowls.jpg" 2>/dev/null || echo "Already renamed or not found: Celadon Lidded Jar and Bowls.jpg"
git mv "IMG_20190622_171212.jpg" "Stacked Moon Face Sculptures.jpg" 2>/dev/null || echo "Already renamed or not found: Stacked Moon Face Sculptures.jpg"
git mv "IMG_20190622_171509.jpg" "Small Green Daylily Vase.jpg" 2>/dev/null || echo "Already renamed or not found: Small Green Daylily Vase.jpg"
git mv "IMG_20190622_183337.jpg" "Daylily Vase Close Up.jpg" 2>/dev/null || echo "Already renamed or not found: Daylily Vase Close Up.jpg"

# Outdoor pottery collections
git mv "IMG_20190627_152235.jpg" "Pottery Collection Rooftop Display.jpg" 2>/dev/null || echo "Already renamed or not found: Pottery Collection Rooftop Display.jpg"
git mv "IMG_20190627_152346.jpg" "White Spiral Bowls Trio.jpg" 2>/dev/null || echo "Already renamed or not found: White Spiral Bowls Trio.jpg"
git mv "IMG_20190627_152512.jpg" "Sunrise Mugs and Brick Vessels.jpg" 2>/dev/null || echo "Already renamed or not found: Sunrise Mugs and Brick Vessels.jpg"
git mv "IMG_20190627_152536.jpg" "White Speckled Spiral Bowl.jpg" 2>/dev/null || echo "Already renamed or not found: White Speckled Spiral Bowl.jpg"
git mv "IMG_20190627_152604.jpg" "Textured Orange and Black Bowl.jpg" 2>/dev/null || echo "Already renamed or not found: Textured Orange and Black Bowl.jpg"
git mv "IMG_20190627_152621.jpg" "White Lidded Jar with Cork.jpg" 2>/dev/null || echo "Already renamed or not found: White Lidded Jar with Cork.jpg"
git mv "IMG_20190627_152651.jpg" "Deep Blue Sun Flask.jpg" 2>/dev/null || echo "Already renamed or not found: Deep Blue Sun Flask.jpg"
git mv "IMG_20190627_152729.jpg" "Faceted Teapot Warm Tones.jpg" 2>/dev/null || echo "Already renamed or not found: Faceted Teapot Warm Tones.jpg"
git mv "IMG_20190627_155829_100.jpg" "Pottery Display Rooftop Wide.jpg" 2>/dev/null || echo "Already renamed or not found: Pottery Display Rooftop Wide.jpg"
git mv "IMG_20190627_155829_101.jpg" "Sunrise Mugs and Brick Vessels Close.jpg" 2>/dev/null || echo "Already renamed or not found: Sunrise Mugs and Brick Vessels Close.jpg"
git mv "IMG_20190627_155829_104.jpg" "White Spiral Bowl Set.jpg" 2>/dev/null || echo "Already renamed or not found: White Spiral Bowl Set.jpg"
git mv "IMG_20190627_155829_105.jpg" "Faceted Teapot Outdoor.jpg" 2>/dev/null || echo "Already renamed or not found: Faceted Teapot Outdoor.jpg"

# Garden and vase pieces
git mv "IMG_20190704_143831.jpg" "Dalmatian Glaze Jar.jpg" 2>/dev/null || echo "Already renamed or not found: Dalmatian Glaze Jar.jpg"
git mv "IMG_20190716_142248.jpg" "Textured Green Moss Vase.jpg" 2>/dev/null || echo "Already renamed or not found: Textured Green Moss Vase.jpg"
git mv "IMG_20190716_142342.jpg" "Sunrise Mugs Paired.jpg" 2>/dev/null || echo "Already renamed or not found: Sunrise Mugs Paired.jpg"
git mv "IMG_20190722_165906.jpg" "Forest Green Moon Mugs Set.jpg" 2>/dev/null || echo "Already renamed or not found: Forest Green Moon Mugs Set.jpg"
git mv "IMG_20190815_132257_811.jpg" "Blue Pedestal Yarn Bowl.jpg" 2>/dev/null || echo "Already renamed or not found: Blue Pedestal Yarn Bowl.jpg"
git mv "IMG_20190821_163531.jpg" "Earth Tone Pourers Trio.jpg" 2>/dev/null || echo "Already renamed or not found: Earth Tone Pourers Trio.jpg"
git mv "IMG_20190821_164058.jpg" "Carved Honey Bowl.jpg" 2>/dev/null || echo "Already renamed or not found: Carved Honey Bowl.jpg"
git mv "IMG_20190821_164121.jpg" "Painted Honey Bowl Interior.jpg" 2>/dev/null || echo "Already renamed or not found: Painted Honey Bowl Interior.jpg"
git mv "IMG_20190821_164423.jpg" "Celadon Carved Cup.jpg" 2>/dev/null || echo "Already renamed or not found: Celadon Carved Cup.jpg"
git mv "IMG_20190821_181245_947.jpg" "Dark Ocean Blue Pour Cup.jpg" 2>/dev/null || echo "Already renamed or not found: Dark Ocean Blue Pour Cup.jpg"
git mv "IMG_20190821_181245_957.jpg" "Blue Dipped Footed Bowl.jpg" 2>/dev/null || echo "Already renamed or not found: Blue Dipped Footed Bowl.jpg"

# Bottles and lidded jars
git mv "IMG_20200119_013147.jpg" "Amber Banded Bottle.jpg" 2>/dev/null || echo "Already renamed or not found: Amber Banded Bottle.jpg"
git mv "IMG_20200119_164109_852.jpg" "Basketweave Lidded Jar.jpg" 2>/dev/null || echo "Already renamed or not found: Basketweave Lidded Jar.jpg"
git mv "IMG_20200119_164109_859.jpg" "Amber Speckled Mugs Pair.jpg" 2>/dev/null || echo "Already renamed or not found: Amber Speckled Mugs Pair.jpg"
git mv "IMG_20200119_165449-01.jpeg" "Moss Green Narrow Vase.jpeg" 2>/dev/null || echo "Already renamed or not found: Moss Green Narrow Vase.jpeg"

# Bowl sets and nesting pieces
git mv "IMG_20200201_195418.jpg" "Cream Square Bowls Nesting.jpg" 2>/dev/null || echo "Already renamed or not found: Cream Square Bowls Nesting.jpg"
git mv "IMG_20200201_195457.jpg" "Cream Nesting Bowls Pair.jpg" 2>/dev/null || echo "Already renamed or not found: Cream Nesting Bowls Pair.jpg"
git mv "IMG_20200201_195620.jpg" "Cream Bowl Interior Spirals.jpg" 2>/dev/null || echo "Already renamed or not found: Cream Bowl Interior Spirals.jpg"
git mv "IMG_20200201_195713.jpg" "Amber Yarn Bowls Pair.jpg" 2>/dev/null || echo "Already renamed or not found: Amber Yarn Bowls Pair.jpg"
git mv "IMG_20200201_195901.jpg" "Amber Yarn Bowl Close View.jpg" 2>/dev/null || echo "Already renamed or not found: Amber Yarn Bowl Close View.jpg"
git mv "IMG_20200201_200035.jpg" "Amber Bowls Geometric Pattern.jpg" 2>/dev/null || echo "Already renamed or not found: Amber Bowls Geometric Pattern.jpg"
git mv "IMG_20200204_172513.jpg" "Amber Geometric Bowls Paired.jpg" 2>/dev/null || echo "Already renamed or not found: Amber Geometric Bowls Paired.jpg"

# Flask and functional vessel sets
git mv "IMG_20200210_172458.jpg" "Amber Eye Bottle.jpg" 2>/dev/null || echo "Already renamed or not found: Amber Eye Bottle.jpg"
git mv "IMG_20200210_172604.jpg" "Amber Eye Bottle and Cream Vase.jpg" 2>/dev/null || echo "Already renamed or not found: Amber Eye Bottle and Cream Vase.jpg"
git mv "IMG_20200210_172814.jpg" "Yarn Bowls and Colander Set.jpg" 2>/dev/null || echo "Already renamed or not found: Yarn Bowls and Colander Set.jpg"
git mv "IMG_20200210_172927.jpg" "Yarn Bowl and Garlic Keeper.jpg" 2>/dev/null || echo "Already renamed or not found: Yarn Bowl and Garlic Keeper.jpg"
git mv "IMG_20200210_173052.jpg" "Amber Bottle and Berry Bowl.jpg" 2>/dev/null || echo "Already renamed or not found: Amber Bottle and Berry Bowl.jpg"
git mv "IMG_20200217_191534.jpg" "Amber Honey Spiral Bowls.jpg" 2>/dev/null || echo "Already renamed or not found: Amber Honey Spiral Bowls.jpg"

# Decorative transfer pieces
git mv "IMG_20200301_195838.jpg" "Mushroom and Koi Flask Collection.jpg" 2>/dev/null || echo "Already renamed or not found: Mushroom and Koi Flask Collection.jpg"
git mv "IMG_20200301_200434.jpg" "Mushroom Flasks Paired.jpg" 2>/dev/null || echo "Already renamed or not found: Mushroom Flasks Paired.jpg"
git mv "IMG_20200301_200547.jpg" "Koi and Monstera Flasks.jpg" 2>/dev/null || echo "Already renamed or not found: Koi and Monstera Flasks.jpg"
git mv "IMG_20200301_200724.jpg" "Carved Foliage Vase Front.jpg" 2>/dev/null || echo "Already renamed or not found: Carved Foliage Vase Front.jpg"
git mv "IMG_20200301_200744.jpg" "Carved Foliage Vase Back.jpg" 2>/dev/null || echo "Already renamed or not found: Carved Foliage Vase Back.jpg"

# Continued pieces
git mv "IMG_20200301_201133.jpg" "Soft Cream Nesting Bowls.jpg" 2>/dev/null || echo "Already renamed or not found: Soft Cream Nesting Bowls.jpg"
git mv "IMG_20200301_201143.jpg" "Soft Cream Bowls Close.jpg" 2>/dev/null || echo "Already renamed or not found: Soft Cream Bowls Close.jpg"
git mv "IMG_20200301_201150-01.jpeg" "Soft Cream Bowl Detail.jpeg" 2>/dev/null || echo "Already renamed or not found: Soft Cream Bowl Detail.jpeg"
git mv "IMG_20200301_201306.jpg" "Carved Wing Mug.jpg" 2>/dev/null || echo "Already renamed or not found: Carved Wing Mug.jpg"

# Berry bowls and colanders
git mv "IMG_20200626_210302.jpg" "Berry Bowl with Drainer.jpg" 2>/dev/null || echo "Already renamed or not found: Berry Bowl with Drainer.jpg"
git mv "IMG_20200626_210340.jpg" "Amber Yarn Bowl Solo.jpg" 2>/dev/null || echo "Already renamed or not found: Amber Yarn Bowl Solo.jpg"
git mv "IMG_20200626_212125.jpg" "Amber Berry Bowl Colander.jpg" 2>/dev/null || echo "Already renamed or not found: Amber Berry Bowl Colander.jpg"
git mv "IMG_20200626_212222.jpg" "Earth Berry Bowl Interior.jpg" 2>/dev/null || echo "Already renamed or not found: Earth Berry Bowl Interior.jpg"
git mv "IMG_20200626_212704.jpg" "Amber Speckled Vase.jpg" 2>/dev/null || echo "Already renamed or not found: Amber Speckled Vase.jpg"

# Monstera and botanical transfers
git mv "IMG_20200629_220700.jpg" "Moss Leaf Teapot.jpg" 2>/dev/null || echo "Already renamed or not found: Moss Leaf Teapot.jpg"
git mv "IMG_20200729_002154-01.jpeg" "Green Moss Flask and Monstera Mug.jpeg" 2>/dev/null || echo "Already renamed or not found: Green Moss Flask and Monstera Mug.jpeg"
git mv "IMG_20200729_002228-01-01.jpeg" "Green Moss Bird Flask.jpeg" 2>/dev/null || echo "Already renamed or not found: Green Moss Bird Flask.jpeg"
git mv "IMG_20200729_002754-01.jpeg" "Botanical Collection Group.jpeg" 2>/dev/null || echo "Already renamed or not found: Botanical Collection Group.jpeg"

echo "Rename script completed. Total: 294 images processed"
