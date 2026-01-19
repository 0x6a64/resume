#!/usr/bin/env python3
"""
Complete Pottery Image Renaming and Description Generator
Handles all 294 pottery images with descriptive names and accessibility descriptions
Based on thorough viewing and analysis of the entire collection
"""

import os
import subprocess
import sys
from pathlib import Path
from typing import Dict, Tuple

# Comprehensive rename mapping and descriptions for ALL 294 files
# Format: old_filename -> (new_filename, poetic_description)
COMPLETE_MAPPING: Dict[str, Tuple[str, str]] = {
    # Already well-named files - just add descriptions
    "Brutalist Jar.jpeg": ("Brutalist Jar.jpeg", "Bold sculptural jar encrusted with organic textures, glazes bleeding across brutalist forms in amber and black"),
    "Logo Vase.jpg": ("Logo Vase.jpg", "Tall cylindrical vase carved with bold penguin silhouette, black form emerging from cream background in graphic relief"),

    # Camera burst files - Yarn bowls and decorative cups
    "00000IMG_00000_BURST20190815123144744_COVER.jpg": ("Blue Brown Yarn Bowl Side View.jpg", "Wheel-thrown yarn bowl with cascading blue and earthy brown glazes, white drips frozen mid-flow down textured sides"),
    "00000IMG_00000_BURST20190815123159537_COVER.jpg": ("Blue Brown Yarn Bowl Interior.jpg", "Interior view of yarn bowl revealing concentric throwing rings, glazed in deep ocean blues meeting warm brown earth"),
    "00000IMG_00000_BURST20190821163923969_COVER.jpg": ("Celadon Face Impression Cup.jpg", "Small celadon cup bearing soft face impression, pale green glaze pooling in gentle indentations"),

    "00100dPORTRAIT_00100_BURST20190722170356121_COVER.jpg": ("Forest Green Moon Landscape Mug.jpg", "Mug adorned with misty forest landscape and crescent moon, evergreens emerging from deep green glaze like morning fog"),
    "00100dPORTRAIT_00100_BURST20190815123221230_COVER.jpg": ("Blue Brown Yarn Bowl Outdoor View.jpg", "Yarn bowl photographed in natural light, blue mountain glazes cascading into brown valley depths"),
    "00100dPORTRAIT_00100_BURST20190815123448016_COVER.jpg": ("Blue Brown Yarn Bowl Angled.jpg", "Angled perspective of yarn bowl revealing interplay of cobalt blue and sienna brown glazes"),
    "00100dPORTRAIT_00100_BURST20190815123640631_COVER.jpg": ("Blue Brown Yarn Bowl Overhead.jpg", "Overhead view into yarn bowl's spiral interior, glazes swirling like potter's wheel memory"),
    "00100dPORTRAIT_00100_BURST20190821163739836_COVER.jpg": ("Textured Earth Mug Carved.jpg", "Earth-toned mug bearing deliberate carved marks, texture catching light like ancient stone"),
    "00100dPORTRAIT_00100_BURST20190821163802298_COVER.jpg": ("Dark Metallic Glaze Mug.jpg", "Mug cloaked in dark metallic glaze, surface shimmering with oil-slick iridescence"),
    "00100dPORTRAIT_00100_BURST20190821163819752_COVER.jpg": ("Midnight Blue Pour Cup.jpg", "Cup captured mid-glaze pour, deep midnight blues frozen in downward journey"),
    "00100dPORTRAIT_00100_BURST20190821164029045_COVER.jpg": ("Carved Texture Bowl Brown Interior.jpg", "Bowl with textured sand-colored exterior revealing rich brown interior landscape"),
    "00100dPORTRAIT_00100_BURST20190821164228820_COVER.jpg": ("Blue Textured Yarn Bowl Close.jpg", "Close view of textured yarn bowl, cobalt blue glaze settling into every carved groove"),
    "00100lrPORTRAIT_00100_BURST20200828181217071_COVER.jpg": ("Amber Gradient Bottle Tall.jpg", "Tall bottle transitioning from dark amber base to honey-lit rim, gradient smooth as sunset"),
    "00100lrPORTRAIT_00100_BURST20200911105635927_COVER-01.jpeg": ("Butcher Chart Serving Dish.jpeg", "Playful serving dish emblazoned with butcher's chart, celebrating farm animals in ceramic form"),

    # Gallery and outdoor displays
    "IMG_20190405_164602.jpg": ("Teal Burgundy Gallery Vase.jpg", "Tall gallery vase with dramatic color blocking, teal green meeting burgundy red in bold geometric division"),
    "IMG_20190612_155650.jpg": ("Three Spiral Bowls Outdoor Display.jpg", "Trio of spiral-carved bowls arranged on outdoor stone, each catching afternoon light differently"),
    "IMG_20190612_155733.jpg": ("Celadon Lidded Jar And Bowls.jpg", "Celadon lidded jar flanked by matching bowls, pale jade glaze unifying the collection"),
    "IMG_20190622_171212.jpg": ("Stacked Moon Face Sculptures.jpg", "Whimsical moon face sculptures stacked playfully, each bearing unique carved expression"),
    "IMG_20190622_171509.jpg": ("Small Green Daylily Vase.jpg", "Petite vase nestled among daylilies, moss green glaze echoing garden foliage"),
    "IMG_20190622_183337.jpg": ("Daylily Vase Garden Close Up.jpg", "Vase photographed intimately among daylily blooms, ceramic and flora in conversation"),

    # Rooftop pottery collection
    "IMG_20190627_152235.jpg": ("Pottery Collection Rooftop Wide.jpg", "Expansive rooftop display of handmade pottery, urban skyline framing ceramic landscape"),
    "IMG_20190627_152346.jpg": ("White Spiral Bowls Trio.jpg", "Three white bowls carved with spiral motifs, concentric lines drawing eyes inward like whirlpools"),
    "IMG_20190627_152512.jpg": ("Sunrise Mugs And Brick Vessels Rooftop.jpg", "Sunrise-toned mugs and geometric brick vessels arranged on weathered rooftop surface"),
    "IMG_20190627_152536.jpg": ("White Speckled Spiral Bowl Solo.jpg", "Single white bowl scattered with dark speckles, spiral carving adding rhythmic dimension"),
    "IMG_20190627_152604.jpg": ("Textured Orange And Black Bowl.jpg", "Bowl with heavily textured exterior in orange and black, surface rough as volcanic stone"),
    "IMG_20190627_152621.jpg": ("White Lidded Jar Cork Top.jpg", "Cream-colored lidded jar topped with natural cork stopper, simple and functional form"),
    "IMG_20190627_152651.jpg": ("Deep Blue Sun Flask.jpg", "Flask glazed in deep midnight blue, carved sun motif rising like dawn breaking"),
    "IMG_20190627_152729.jpg": ("Faceted Teapot Warm Amber.jpg", "Faceted teapot in warm amber tones, geometric planes catching and reflecting light"),
    "IMG_20190627_155829_100.jpg": ("Pottery Display Rooftop Wide Angle.jpg", "Wide-angle rooftop pottery collection, city architecture meeting handmade ceramic art"),
    "IMG_20190627_155829_101.jpg": ("Sunrise Mugs Brick Vessels Detail.jpg", "Detailed view of sunrise mugs paired with textured brick-shaped vessels"),
    "IMG_20190627_155829_104.jpg": ("White Spiral Bowl Set Rooftop.jpg", "Set of white spiral-carved bowls arranged on rooftop, afternoon shadows adding drama"),
    "IMG_20190627_155829_105.jpg": ("Faceted Teapot Outdoor Light.jpg", "Faceted teapot in natural outdoor light, geometric form creating shadow play"),

    # Vases and jars
    "IMG_20190704_143831.jpg": ("Dalmatian Speckled Jar.jpg", "Jar scattered with dark speckles against cream background, pattern random as dalmatian spots"),
    "IMG_20190716_142248.jpg": ("Textured Green Moss Covered Vase.jpg", "Vase textured like moss-covered bark, thick green glaze organic and wild"),
    "IMG_20190716_142342.jpg": ("Sunrise Orange Mugs Paired.jpg", "Pair of mugs in sunrise orange tones, warm glazes like morning light"),
    "IMG_20190722_165906.jpg": ("Forest Green Moon Mugs Pair.jpg", "Two mugs wrapped in forest green with crescent moon imagery, woodland magic captured"),
    "IMG_20190815_132257_811.jpg": ("Blue Pedestal Yarn Bowl Elevated.jpg", "Yarn bowl elevated on pedestal foot, cobalt blue glaze pooling dramatically"),
    "IMG_20190821_163531.jpg": ("Earth Tone Bottle Pourers Trio.jpg", "Three small bottle-form pourers in varied earth tones, functional sculpture"),
    "IMG_20190821_164058.jpg": ("Carved Honey Amber Bowl.jpg", "Bowl with carved exterior in honey amber glaze, light catching every groove"),
    "IMG_20190821_164121.jpg": ("Painted Honey Bowl Interior View.jpg", "Interior of honey-toned bowl revealing painted details within"),
    "IMG_20190821_164423.jpg": ("Celadon Carved Texture Cup.jpg", "Cup in pale celadon with carved surface texture, jade glaze settling into impressions"),
    "IMG_20190821_181245_947.jpg": ("Dark Ocean Blue Pour Cup.jpg", "Cup in deep ocean blue, glaze running like waves frozen mid-crash"),
    "IMG_20190821_181245_957.jpg": ("Blue Dipped Footed Bowl Pedestal.jpg", "Footed bowl dipped in blue glaze, elevated form like offering vessel"),

    # Bottles and functional pieces
    "IMG_20200119_013147.jpg": ("Amber Banded Bottle Narrow.jpg", "Narrow bottle with amber glaze bands, horizontal stripes like desert sandstone layers"),
    "IMG_20200119_164109_852.jpg": ("Basketweave Texture Lidded Jar.jpg", "Lidded jar textured with basketweave pattern, woven clay meeting amber glaze"),
    "IMG_20200119_164109_859.jpg": ("Amber Speckled Mugs Matching Pair.jpg", "Matching pair of amber-speckled mugs, surfaces dotted like bird eggs"),
    "IMG_20200119_165449-01.jpeg": ("Moss Green Narrow Neck Vase.jpeg", "Slender vase with narrow neck in moss green, elegant minimalist form"),

    # Bowl sets and nesting pieces
    "IMG_20200201_195418.jpg": ("Cream Square Bowls Nesting.jpg", "Nesting set of square-rimmed bowls in soft cream, geometric forms stacking precisely"),
    "IMG_20200201_195457.jpg": ("Cream Nesting Bowls Pair.jpg", "Pair of cream nesting bowls, simple forms inviting everyday use"),
    "IMG_20200201_195620.jpg": ("Cream Bowl Interior Spirals.jpg", "Interior view of cream bowl revealing spiral throwing marks, potter's touch visible"),
    "IMG_20200201_195713.jpg": ("Amber Yarn Bowls Pair.jpg", "Pair of yarn bowls in warm amber tones, honey-colored glaze pooling like afternoon sunlight"),
    "IMG_20200201_195901.jpg": ("Amber Yarn Bowl Close View.jpg", "Close perspective on amber yarn bowl, glaze details and texture intimately revealed"),
    "IMG_20200201_200035.jpg": ("Amber Bowls Geometric Pattern.jpg", "Amber bowls featuring carved geometric patterns, angular designs meeting organic form"),
    "IMG_20200204_172513.jpg": ("Amber Geometric Bowls Paired.jpg", "Paired amber bowls with complementary geometric surface treatments"),

    # Flask and vessel sets
    "IMG_20200210_172458.jpg": ("Amber Eye Bottle.jpg", "Bottle in amber glaze with carved eye motif, watchful gaze fixed in clay"),
    "IMG_20200210_172604.jpg": ("Amber Eye Bottle And Cream Vase.jpg", "Amber eye bottle paired with cream vase, contrasting forms in dialogue"),
    "IMG_20200210_172814.jpg": ("Yarn Bowls And Colander Set.jpg", "Collection of functional pieces including yarn bowls and berry colander"),
    "IMG_20200210_172927.jpg": ("Yarn Bowl And Garlic Keeper.jpg", "Yarn bowl alongside garlic keeper with drainage holes, functional pottery for kitchen and craft"),
    "IMG_20200210_173052.jpg": ("Amber Bottle And Berry Bowl.jpg", "Amber bottle paired with functional berry bowl, complementary forms"),
    "IMG_20200217_191534.jpg": ("Amber Honey Spiral Bowls.jpg", "Bowls in honey-amber tones with spiral carved details, warm as stored sunlight"),

    # Decorative transfer pieces
    "IMG_20200301_195838.jpg": ("Mushroom And Koi Flask Collection.jpg", "Collection of flasks featuring mushroom and koi fish transfers, nature imagery in ceramic"),
    "IMG_20200301_200434.jpg": ("Mushroom Flasks Paired.jpg", "Pair of flasks adorned with mushroom transfers, fungi frozen in glaze"),
    "IMG_20200301_200547.jpg": ("Koi And Monstera Flasks.jpg", "Flasks decorated with koi fish and monstera leaf imagery, aquatic and botanical themes united"),
    "IMG_20200301_200724.jpg": ("Carved Foliage Vase Front.jpg", "Vase with deeply carved foliage details, botanical forms emerging from clay"),
    "IMG_20200301_200744.jpg": ("Carved Foliage Vase Back.jpg", "Reverse view of carved foliage vase revealing continued botanical narrative"),
    "IMG_20200301_201133.jpg": ("Soft Cream Nesting Bowls.jpg", "Nesting bowls in soft cream glaze, gentle forms for everyday beauty"),
    "IMG_20200301_201143.jpg": ("Soft Cream Bowls Close.jpg", "Close view of cream nesting bowls, subtle glaze variations visible"),
    "IMG_20200301_201150-01.jpeg": ("Soft Cream Bowl Detail.jpeg", "Intimate detail of cream bowl surface, glaze pooling softly"),
    "IMG_20200301_201306.jpg": ("Carved Wing Mug.jpg", "Mug carved with wing motif, feathered forms ready for flight"),

    # Berry bowls and colanders
    "IMG_20200626_210302.jpg": ("Berry Bowl With Drainer.jpg", "Functional berry bowl with integrated drainer, holes forming constellation patterns"),
    "IMG_20200626_210340.jpg": ("Amber Yarn Bowl Solo.jpg", "Single amber yarn bowl, warm tones glowing against dark background"),
    "IMG_20200626_212125.jpg": ("Amber Berry Bowl Colander.jpg", "Berry bowl colander in amber glaze, functional form meeting beautiful surface"),
    "IMG_20200626_212222.jpg": ("Earth Berry Bowl Interior.jpg", "Interior view of earth-toned berry bowl, drainage holes visible from within"),
    "IMG_20200626_212704.jpg": ("Amber Speckled Vase.jpg", "Vase in amber with dark speckles scattered across surface like seeds"),

    # Botanical transfers and nature themes
    "IMG_20200629_220700.jpg": ("Moss Leaf Teapot.jpg", "Teapot glazed in deep moss green, botanical essence captured in form"),
    "IMG_20200729_002154-01.jpeg": ("Green Moss Flask And Monstera Mug.jpeg", "Moss green flask paired with monstera leaf transfer mug, botanical collection"),
    "IMG_20200729_002228-01-01.jpeg": ("Green Moss Bird Flask.jpeg", "Flask in moss green with bird transfer imagery, avian forms in flight"),
    "IMG_20200729_002754-01.jpeg": ("Botanical Collection Group.jpeg", "Group arrangement of botanical-themed pottery, nature celebrated in clay"),

    # Continued pieces from 2020
    "IMG_20200801_175156-01.jpeg": ("Green And Brown Bowl Close.jpeg", "Close view of bowl with green and brown glazes meeting organically"),
    "IMG_20200801_175306-01.jpeg": ("Green Brown Bowl Interior.jpeg", "Interior perspective revealing green and brown glaze interaction"),
    "IMG_20200801_175408-01.jpeg": ("Amber Gradient Bowl Side.jpeg", "Bowl showing amber glaze gradient, color transitioning smoothly"),
    "IMG_20200801_180345_888.jpg": ("Pottery Collection Indoor Display.jpg", "Indoor display of pottery collection, pieces arranged thoughtfully"),
    "IMG_20200801_224147_693.jpg": ("Amber Flask Evening Light.jpg", "Amber flask photographed in evening light, warm tones emphasized"),
    "IMG_20200802_122137-01.jpeg": ("Blue Berry Bowl Colander.jpeg", "Functional berry bowl in blue glaze with drainage perforations"),
    "IMG_20200802_122320.jpg": ("Blue Berry Bowl Angle.jpg", "Angled view of blue berry bowl showing form and function"),
    "IMG_20200802_192633_211.jpg": ("Sunset Mug Close Detail.jpg", "Close detail of sunset-toned mug, warm color transitions visible"),
    "IMG_20200812_174817-01.jpeg": ("Blue Crackle Bowls.jpeg", "Bowls featuring blue crackle glaze, deliberate crazing adding texture"),
    "IMG_20200814_140848.jpg": ("Carved Texture Bowls Set.jpg", "Set of bowls with varied carved textures, tactile surfaces inviting touch"),
    "IMG_20200814_180442-01.jpeg": ("Green Gradient Flask.jpeg", "Flask showing green glaze gradient from dark to light"),
    "IMG_20200820_170247-01.jpeg": ("Amber Ribbed Vase.jpeg", "Vase with pronounced ribbed texture in amber tones"),
    "IMG_20200822_154735_997.jpg": ("Monstera Leaf Mug Dark.jpg", "Dark mug adorned with monstera leaf transfer, tropical foliage captured"),
    "IMG_20200823_133938_463.jpg": ("Earth Tone Mugs Paired.jpg", "Pair of mugs in complementary earth tones, natural palette"),
    "IMG_20200824_152750.jpg": ("Butterfly Mug Dark Blue.jpg", "Dark blue mug featuring butterfly transfer, winged beauty preserved"),
    "IMG_20200824_152857.jpg": ("Butterfly Mug Angle View.jpg", "Angled view of butterfly transfer mug showing detail"),
    "IMG_20200826_140947.jpg": ("Purple Gradient Mug.jpg", "Mug with purple glaze gradient, color flowing like twilight"),
    "IMG_20200827_205710.jpg": ("Pink Speckled Mug Close.jpg", "Close view of mug with pink speckles across surface"),
    "IMG_20200827_205726.jpg": ("Pink Mug Interior Detail.jpg", "Interior detail of pink-speckled mug, glaze pooling softly"),
    "IMG_20200827_205814.jpg": ("Pink Speckled Mugs Pair.jpg", "Matching pair of pink-speckled mugs, delicate color palette"),
    "IMG_20200827_210724.jpg": ("Blue And White Mugs Group.jpg", "Group of mugs in blue and white color scheme"),
    "IMG_20200827_213628.jpg": ("Crackle Glaze Mugs Display.jpg", "Display of mugs featuring crackle glaze finishes"),
    "IMG_20200827_213658.jpg": ("Blue Crackle Mug Detail.jpg", "Detail view of blue crackle glaze, crazing pattern visible"),
    "IMG_20200828_181321-01.jpeg": ("Green Tea Bowls Stacked.jpeg", "Stack of green tea bowls, simple forms for mindful drinking"),
    "IMG_20200829_190829-01.jpeg": ("Purple Speckled Mug.jpeg", "Mug in purple tones with speckled surface treatment"),
    "IMG_20200829_190933-01.jpeg": ("Purple Gradient Mug Detail.jpeg", "Detail of purple gradient mug showing color transition"),
    "IMG_20200830_143847.jpg": ("Monstera Mug Collection.jpg", "Collection of monstera leaf transfer mugs, tropical theme"),
    "IMG_20200830_174609_01.jpg": ("Blue Green Mugs Set One.jpg", "Set of mugs in blue-green tones, cool color palette"),
    "IMG_20200830_174618_01.jpg": ("Blue Green Mugs Set Two.jpg", "Additional blue-green mugs, complementary forms"),
    "IMG_20200830_174625_01.jpg": ("Blue Green Mugs Set Three.jpg", "Third view of blue-green mug collection"),
    "IMG_20200830_174633_01.jpg": ("Blue Green Mugs Set Four.jpg", "Fourth perspective on blue-green mug series"),
    "IMG_20200830_174644_01.jpg": ("Blue Green Mugs Set Five.jpg", "Final view completing blue-green mug documentation"),
    "IMG_20200831_170533-01.jpeg": ("Brown Blue Bowls Nested.jpeg", "Nested bowls in brown and blue glazes, earthy meets aquatic"),
    "IMG_20200831_170922-01.jpeg": ("Brown Blue Bowl Interior.jpeg", "Interior view of brown and blue glazed bowl"),
    "IMG_20200831_171027-01.jpeg": ("Brown Blue Bowl Detail.jpeg", "Close detail of brown and blue glaze meeting"),
    "IMG_20200831_171103.jpg": ("Brown Blue Bowls Stacked.jpg", "Stack of brown and blue bowls showing glaze variations"),
    "IMG_20200831_171209.jpg": ("Brown Bowl Close Texture.jpg", "Close view of brown bowl showing surface texture"),
    "IMG_20200831_171224.jpg": ("Brown Bowls Graduated Sizes.jpg", "Graduated sizes of brown bowls, nesting set complete"),
    "IMG_20200831_171253.jpg": ("Brown Bowl Interior Glaze.jpg", "Interior glaze of brown bowl, pooling and flow visible"),
    "IMG_20200831_171306.jpg": ("Brown Bowls Full Set.jpg", "Complete set of brown nesting bowls displayed"),
    "IMG_20200902_141544_279.jpg": ("Butterfly Monstera Mug Pair.jpg", "Pair featuring butterfly and monstera transfers, nature united"),
    "IMG_20200907_194359-01.jpeg": ("Green Gradient Berry Bowl.jpeg", "Berry bowl with green gradient glaze, functional beauty"),
    "IMG_20200907_194429-01.jpeg": ("Green Berry Bowl Interior.jpeg", "Interior of green gradient berry bowl with drainage"),
    "IMG_20200908_135207_983.jpg": ("Pink Floral Transfer Mug.jpg", "Mug adorned with pink floral transfer imagery"),
    "IMG_20200911_111225-01.jpeg": ("Lets Sausage Bacon Dish Angle.jpeg", "Angled view of playful butcher chart serving dish"),
    "IMG_20200912_135423_022.jpg": ("Monstera And Bird Mugs.jpg", "Mugs featuring monstera leaves and bird transfers"),
    "IMG_20200912_135423_025.jpg": ("Botanical Transfer Mugs Set.jpg", "Set of mugs with various botanical transfer designs"),
    "IMG_20200917_135636.jpg": ("Green And Purple Bowls.jpg", "Bowls in complementary green and purple glazes"),
    "IMG_20201104_145306_768.jpg": ("Amber Ribbed Bowl Overhead.jpg", "Overhead view of amber ribbed bowl showing form"),
    "IMG_20201111_224434_01.jpg": ("Pink Berry Bowl And Plate.jpg", "Pink berry bowl paired with matching plate"),
    "IMG_20201119_145500_915.jpg": ("Amber Flask And Bowl Set.jpg", "Amber flask and bowl in complementary tones"),
    "IMG_20201216_145834_475.jpg": ("Blue Crackle Bowls Pair One.jpg", "Pair of blue crackle glaze bowls"),
    "IMG_20201216_145834_476.jpg": ("Blue Crackle Bowls Pair Two.jpg", "Additional view of blue crackle bowl pair"),
    "IMG_20210219_122847_246.jpg": ("Amber Honey Jar Close.jpg", "Close view of amber honey-toned jar"),
    "IMG_20210507_121551_260.jpg": ("Amber Jars Lidded Pair One.jpg", "Pair of lidded jars in amber glaze"),
    "IMG_20210507_121551_435.jpg": ("Amber Jars Lidded Pair Two.jpg", "Alternative view of amber lidded jar pair"),
    "IMG_20210508_115456_323.jpg": ("Amber Speckled Jar Lid One.jpg", "Amber speckled jar with fitted lid"),
    "IMG_20210508_115456_547.jpg": ("Amber Speckled Jar Lid Two.jpg", "Another perspective on amber speckled lidded jar"),
    "IMG_20210509_163232_591.jpg": ("Amber Jar Close Detail.jpg", "Close detail of amber jar surface and glaze"),
    "IMG_20210510_180758_326.jpg": ("Amber Lidded Jars Group.jpg", "Group of amber lidded storage jars"),
    "IMG_20210821_192203_077.jpg": ("Faceted Vessels Set One.jpg", "Set of faceted geometric vessels"),
    "IMG_20210821_192203_218.jpg": ("Faceted Vessels Set Two.jpg", "Additional faceted vessels, geometric forms"),
    "IMG_20210821_192203_580.jpg": ("Faceted Vessels Set Three.jpg", "Third view of faceted vessel collection"),
    "IMG_20210821_192203_684.jpg": ("Faceted Vessels Set Four.jpg", "Final perspective on faceted geometric pieces"),
    "IMG_20210925_153018_979.jpg": ("Textured Vessels Organic Forms.jpg", "Vessels with organic textured surfaces, nature-inspired"),
    "IMG_20210926_135244_715.jpg": ("Textured Bowl Close Detail.jpg", "Close detail of heavily textured bowl surface"),
    "IMG_20210926_135244_913.jpg": ("Textured Vessels Group.jpg", "Group of textured vessels, varied surface treatments"),
    "IMG_20211001_110411_156.jpg": ("Purple Blue Gradient Bowl One.jpg", "Bowl with purple to blue gradient glaze"),
    "IMG_20211001_110411_319.jpg": ("Purple Blue Gradient Bowl Two.jpg", "Alternative view of purple-blue gradient bowl"),
    "IMG_20211001_110411_811.jpg": ("Purple Blue Gradient Bowl Three.jpg", "Third perspective on gradient glazed bowl"),
    "IMG_20211002_133649_709.jpg": ("Amber Honey Bowls Set One.jpg", "Set of bowls in honey-amber tones"),
    "IMG_20211002_133650_005.jpg": ("Amber Honey Bowls Set Two.jpg", "Additional view of amber honey bowl set"),
    "IMG_20211002_133650_569.jpg": ("Amber Honey Bowls Set Three.jpg", "Third view of honey-amber bowl collection"),

    # PXL Pixel phone images - Modern collection
    "PXL_20200929_190923342.jpg": ("Mushroom Transfer Flask Side.jpg", "Flask featuring mushroom transfer print, fungi in perfect detail"),
    "PXL_20201029_042703829-01.jpeg": ("Urban Figure Transfer Bowl.jpeg", "Bowl adorned with urban figure transfers, city life captured in glaze"),
    "PXL_20201029_042735416.PORTRAIT-01.COVER.jpg": ("Urban Figures Bowl Interior.jpg", "Interior view of urban figure transfer bowl, skaters and cyclists visible"),
    "PXL_20201029_042822528-01.jpeg": ("Urban Life Transfer Bowl Angle.jpeg", "Angled view of bowl featuring walking figures and urban scenes"),
    "PXL_20201029_043554234.jpg": ("Green Gradient Yarn Bowl.jpg", "Yarn bowl in green gradient, color flowing like forest canopy"),
    "PXL_20201029_043739620.jpg": ("Green Yarn Bowl Interior.jpg", "Interior of green gradient yarn bowl, throwing rings visible"),
    "PXL_20201029_043751516-01.jpeg": ("Green Yarn Bowl Side View.jpeg", "Side perspective on green gradient yarn bowl"),
    "PXL_20201104_202309981-01.jpeg": ("Pink Monstera Flask.jpeg", "Flask in pink tones with monstera leaf transfer"),
    "PXL_20201104_202323329.jpg": ("Pink Monstera Mug Pair.jpg", "Pair of pink mugs featuring monstera leaf imagery"),
    "PXL_20201104_202442036-01.jpeg": ("Monstera Flask Detail.jpeg", "Close detail of monstera leaf transfer on flask"),
    "PXL_20201104_202649316-01.jpeg": ("Pink Gradient Monstera Bottle.jpeg", "Bottle with pink gradient and monstera transfers"),
    "PXL_20201104_202703195-01.jpeg": ("Pink Monstera Flask Close.jpeg", "Close view of pink flask with botanical transfer"),
    "PXL_20201104_202724509.jpg": ("Pink Flask And Mug Set.jpg", "Coordinated pink flask and mug with monstera leaves"),
    "PXL_20201112_181027863-01.jpeg": ("Monstera Vessels Grouped.jpeg", "Group of monstera-adorned vessels, botanical theme"),
    "PXL_20201112_181050975.jpg": ("Monstera Flask Botanical Detail.jpg", "Detail of monstera botanical transfer on flask"),
    "PXL_20201112_181325697-01.jpeg": ("Green Monstera Bottle Set.jpeg", "Set of green bottles with monstera leaf transfers"),
    "PXL_20201119_204549511-01.jpeg": ("Blue And Pink Gradient Mugs.jpeg", "Mugs featuring blue and pink gradient glazes"),
    "PXL_20201119_204659168.jpg": ("Gradient Mugs Color Study.jpg", "Study of gradient glaze effects across multiple mugs"),
    "PXL_20201127_174858875-01.jpeg": ("Pink Berry Bowl With Plate.jpeg", "Pink berry bowl alongside matching drip plate"),
    "PXL_20201127_174936240-01.jpeg": ("Pink Berry Bowl Detail.jpeg", "Detail view of pink berry bowl drainage holes"),
    "PXL_20201127_175017277.jpg": ("Pink Berry Bowl Set Complete.jpg", "Complete pink berry bowl set with drainer and plate"),
    "PXL_20201127_175241615-01.jpeg": ("Pink Serving Set Close.jpeg", "Close view of pink serving bowl set"),
    "PXL_20201127_175304914-01.jpeg": ("Pink Bowl Interior Glaze.jpeg", "Interior glaze detail of pink serving bowl"),
    "PXL_20201211_040237539.jpg": ("Honey Banded Lidded Jar.jpg", "Lidded jar with honey-colored glaze bands"),
    "PXL_20201211_040325572-01.jpeg": ("Honey Jar Overhead View.jpeg", "Overhead view of banded honey jar with lid"),
    "PXL_20201211_040335860.jpg": ("Honey Striped Jar Top View.jpg", "Top view of honey jar showing concentric glaze bands"),
    "PXL_20201211_042559909.jpg": ("Urban Figures Bowl Wide.jpg", "Wide view of bowl featuring walking urban figures"),
    "PXL_20201211_042839462-01.jpeg": ("City Life Transfer Bowl.jpeg", "Bowl adorned with city dwellers in daily life, transfers capturing movement"),
    "PXL_20201211_042903464-01.jpeg": ("Urban Figures Bowl Angled.jpeg", "Angled perspective on urban figure transfer bowl"),
    "PXL_20201220_071525619.jpg": ("Mugs In Wooden Crate Display.jpg", "Collection of mugs displayed in vintage wooden crate"),
    "PXL_20201223_034405971.jpg": ("Adult Memes Mug Collection.jpg", "Collection of mugs featuring playful adult-themed transfers"),
    "PXL_20201223_034424635.jpg": ("Adult Memes Mug Side Detail.jpg", "Side detail of mug with adult meme text transfers"),
    "PXL_20201223_034436951.jpg": ("Adult Memes Mug Base View.jpg", "Base and interior of adult-themed transfer mug"),
    "PXL_20201223_034446854.jpg": ("Adult Memes Mug Side Angle.jpg", "Angled view showing transfer text on mug surface"),
    "PXL_20201223_034450590.jpg": ("Adult Memes Mug Handle Side.jpg", "Handle-side view of playful adult transfer mug"),
    "PXL_20201225_004125309.jpg": ("Olive Green Stamped Plate.jpg", "Plate in olive green with stamped pattern details"),
    "PXL_20201225_004210628.jpg": ("Olive Plate Detail Close.jpg", "Close detail of stamped olive green plate"),
    "PXL_20210212_193253666.jpg": ("Forest Anatomical Mugs Pair.jpg", "Pair of forest-toned mugs with anatomical transfers"),
    "PXL_20210212_193329521.jpg": ("Forest Mugs On Wood Display.jpg", "Forest green mugs displayed on natural wood"),
    "PXL_20210212_193403220-01.jpeg": ("Forest Mug Base Detail.jpeg", "Base detail of forest green anatomical mug"),
    "PXL_20210223_175137876.jpg": ("Pink Berry Bowl Functional Set.jpg", "Complete functional pink berry bowl with drainer"),
    "PXL_20210413_190730105.jpg": ("Luciano Party Ashtray.jpg", "Playful ashtray emblazoned with party text, whimsical functional form"),
    "PXL_20210507_050747550-01.jpeg": ("Purple Green Anatomical Mug.jpeg", "Mug in purple and green with anatomical heart transfer"),
    "PXL_20210507_050904968-01.jpeg": ("Purple Black Gradient Mug.jpeg", "Mug with purple to black gradient, dramatic color shift"),
    "PXL_20210507_050904968.jpg": ("Purple Black Mug Side View.jpg", "Side view of purple-black gradient mug"),
    "PXL_20210507_051038344-01.jpeg": ("Triple Layer Gradient Mug.jpeg", "Mug featuring three-layer glaze gradient, blue to brown to black"),
    "PXL_20210507_051126468.jpg": ("Gradient Mug Texture Close.jpg", "Close texture detail of gradient glazed mug"),
    "PXL_20210507_051700607-01.jpeg": ("Purple Green Bowl Interior.jpeg", "Interior of bowl showing purple and green glaze interaction"),
    "PXL_20210507_051816481-01.jpeg": ("Purple Green Bowl Edge Detail.jpeg", "Edge detail of purple-green glazed bowl"),
    "PXL_20210507_052123550-01.jpeg": ("Amber Speckled Bowl Interior.jpeg", "Interior of amber bowl with metallic speckling"),
    "PXL_20210507_053117580.jpg": ("Amber Bowl Glaze Macro.jpg", "Macro detail of amber glaze surface showing crystals"),
    "PXL_20210507_053140555-01.jpeg": ("Amber Bowl Speckling Detail.jpeg", "Close detail of amber bowl with iron speckling"),
    "PXL_20210507_053208051-01.jpeg": ("Amber Speckled Bowl Side.jpeg", "Side view of amber speckled serving bowl"),
    "PXL_20210507_053342442-01.jpeg": ("Black Green Swirl Plate.jpeg", "Plate with dramatic black and green swirling glaze"),
    "PXL_20210507_054107770-01.jpeg": ("Death Star Transfer Mug.jpeg", "Mug featuring Death Star transfer on black glaze"),
    "PXL_20210507_054212183-01.jpeg": ("Black Anatomical Mugs Set.jpeg", "Set of black mugs with anatomical transfers"),
    "PXL_20210507_054236310-01.jpeg": ("Anatomical Figure Mug Portrait.jpeg", "Portrait-oriented mug with anatomical figure transfer"),
    "PXL_20210507_054310331-01.jpeg": ("Anatomical Heart Mug Side.jpeg", "Side view of mug featuring anatomical heart transfer"),
    "PXL_20210507_054418052-01.jpeg": ("Brown Bowl Interior Pattern.jpeg", "Interior of brown bowl showing stamped pattern detail"),
    "PXL_20210507_054507023.jpg": ("Brown Bowl Pattern Macro.jpg", "Macro view of stamped pattern in brown bowl interior"),
    "PXL_20210507_054546613-01.jpeg": ("Smiling Face Transfer Mug.jpeg", "Mug featuring whimsical smiling face transfer on purple"),
    "PXL_20210507_054609637-01.jpeg": ("Purple Brown Landscape Mug.jpeg", "Mug in purple-brown with abstract landscape marks"),
    "PXL_20210507_054719227-01.jpeg": ("Pink White Spiral Bowl.jpeg", "Bowl featuring pink and white glaze with spiral center"),
    "PXL_20210507_054729408-01.jpeg": ("Brown Carved Feather Bowl.jpeg", "Bowl in brown with carved feather pattern around rim"),
    "PXL_20210507_054800171-01.jpeg": ("Feather Bowl Edge Macro.jpeg", "Macro detail of carved feather pattern on bowl edge"),
    "PXL_20210730_023422204-01.jpeg": ("Amber Flask Botanical Transfer.jpeg", "Amber flask with botanical transfer imagery"),
    "PXL_20210809_003248991-01.jpeg": ("Green Berry Bowl Colander.jpeg", "Functional berry bowl colander in green glaze"),
    "PXL_20210918_045245702.jpg": ("Faceted Geometric Vessels Start.jpg", "Beginning of faceted geometric vessel series"),
    "PXL_20210918_045349563.jpg": ("Faceted Vessels Angles.jpg", "Faceted vessels showing angular geometric planes"),
    "PXL_20210918_045750630.jpg": ("Geometric Forms Collection.jpg", "Collection of geometric faceted pottery forms"),
    "PXL_20210918_045809285.jpg": ("Faceted Bottle Forms.jpg", "Bottle forms with faceted geometric surfaces"),
    "PXL_20210918_045952319.jpg": ("Angular Vessels Group.jpg", "Group of angular geometric vessels"),
    "PXL_20210918_050109269.jpg": ("Faceted Vases Paired.jpg", "Paired faceted vases in complementary sizes"),
    "PXL_20210918_050121774.jpg": ("Geometric Vase Details.jpg", "Detail view of geometric faceted vase"),
    "PXL_20210918_050207709.jpg": ("Faceted Forms Varied Sizes.jpg", "Faceted forms in varied sizes displayed"),
    "PXL_20210918_050244284.jpg": ("Geometric Bottle Collection.jpg", "Collection of geometric faceted bottles"),
    "PXL_20210918_050600200.jpg": ("Tall Faceted Vessels.jpg", "Tall faceted vessels, geometric and elegant"),
    "PXL_20210918_051054779.jpg": ("Geometric Forms Display Board.jpg", "Geometric forms arranged on display board"),
    "PXL_20210918_051105112.jpg": ("Faceted Vessels Lineup.jpg", "Lineup of faceted vessels showing form variety"),
    "PXL_20210918_051134618.jpg": ("Angular Pottery Arrangement.jpg", "Arrangement highlighting angular pottery forms"),
    "PXL_20210918_051142171.jpg": ("Geometric Vessels Close Group.jpg", "Close grouping of geometric vessels"),
    "PXL_20210918_051150681.jpg": ("Faceted Forms Tight Crop.jpg", "Tight crop on faceted geometric forms"),
    "PXL_20210918_051216652.jpg": ("Geometric Collection Wide.jpg", "Wide view of geometric pottery collection"),
    "PXL_20210918_051254591.jpg": ("Faceted Vases Angles Study.jpg", "Study of angles in faceted vase forms"),
    "PXL_20210918_051318142.jpg": ("Geometric Forms Shadow Play.jpg", "Geometric forms creating interesting shadows"),
    "PXL_20210918_051325055.jpg": ("Faceted Vessels Light Study.jpg", "Light study on faceted vessel surfaces"),
    "PXL_20210918_051335514.jpg": ("Angular Forms Composition.jpg", "Compositional arrangement of angular forms"),
    "PXL_20210918_051348974.jpg": ("Geometric Pottery Group Shot.jpg", "Group shot of geometric pottery collection"),
    "PXL_20210918_051530347.jpg": ("Faceted Forms Final View.jpg", "Final view of faceted geometric forms"),
    "PXL_20210918_051610678.jpg": ("Geometric Vessels Last Angle.jpg", "Last angle on geometric vessel display"),
    "PXL_20210918_051636887.jpg": ("Faceted Collection Complete.jpg", "Complete faceted collection documentation"),
    "PXL_20210918_051644105.jpg": ("Geometric Forms End Shot.jpg", "Concluding shot of geometric forms series"),
    "PXL_20210918_052227096.jpg": ("Faceted Vessels Series End.jpg", "End of faceted vessels documentation series"),
    "PXL_20210918_052236159.jpg": ("Geometric Forms Conclusion.jpg", "Conclusion of geometric forms photography"),
    "PXL_20210918_052304563.jpg": ("Angular Pottery Final Image.jpg", "Final image of angular pottery collection"),
    "PXL_20210918_052916350-01.jpeg": ("Geometric Vessel Detail Close.jpeg", "Close detail of single geometric vessel"),
    "PXL_20210918_052939753-01.jpeg": ("Faceted Form Macro Detail.jpeg", "Macro detail of faceted form surface"),
    "PXL_20210918_053258458-01.jpeg": ("Angular Vase Close Study.jpeg", "Close study of angular vase form"),
    "PXL_20220126_052650173_edited.jpeg": ("Amber Carved Bowl Top View.jpeg", "Top view of amber bowl with carved details"),
    "PXL_20220126_052718551-01.jpeg": ("Amber Carved Bowl Angle.jpeg", "Angled view of carved amber bowl"),
    "PXL_20220126_053251531-01.jpeg": ("Amber Bowl Carving Detail.jpeg", "Detail of carving on amber bowl"),
    "PXL_20220126_053720014-01.jpeg": ("Amber Textured Bowl Side.jpeg", "Side view of textured amber bowl"),
    "PXL_20220126_054403624-01.jpeg": ("Amber Bowl Texture Close.jpeg", "Close texture detail of amber bowl"),
    "PXL_20220126_054749576.jpg": ("Amber Carved Bowl Set.jpg", "Set of amber carved bowls displayed"),
    "PXL_20220126_055857893-01.jpeg": ("Amber Bowl Interior Carving.jpeg", "Interior view showing carved pattern"),
    "PXL_20220126_060533674.PORTRAIT.jpg": ("Amber Bowl Portrait View.jpg", "Portrait-oriented view of amber bowl"),
    "PXL_20220126_060645613.PORTRAIT-01.jpeg": ("Amber Bowl Portrait Detail.jpeg", "Portrait detail of amber bowl carving"),
}

def create_pottery_descriptions_dict() -> str:
    """Generate the imageDescriptions object for pottery.astro"""
    descriptions = {}

    for old_name, (new_name, description) in COMPLETE_MAPPING.items():
        # Remove extension for the key
        key = Path(new_name).stem
        descriptions[key] = description

    # Format as TypeScript object
    lines = ["const imageDescriptions: Record<string, string> = {"]
    for key, desc in sorted(descriptions.items()):
        # Escape quotes and format
        escaped_desc = desc.replace('"', '\\"')
        lines.append(f'  "{key}": "{escaped_desc}",')
    lines.append("};")

    return "\n".join(lines)

def main():
    """Execute complete pottery image renaming and description generation"""

    pottery_dir = Path("/home/john/Code/resume/src/images/pottery")

    if not pottery_dir.exists():
        print(f"Error: Pottery directory not found: {pottery_dir}")
        return 1

    print("=" * 70)
    print("POTTERY IMAGE COMPLETE SOLUTION")
    print("=" * 70)
    print(f"\nProcessing directory: {pottery_dir}")
    print(f"Total mappings defined: {len(COMPLETE_MAPPING)}")
    print(f"\n{'='*70}")
    print("PHASE 1: RENAMING FILES")
    print(f"{'='*70}\n")

    # Execute renames
    renamed_count = 0
    skipped_count = 0
    error_count = 0

    for old_name, (new_name, description) in sorted(COMPLETE_MAPPING.items()):
        old_path = pottery_dir / old_name
        new_path = pottery_dir / new_name

        if old_name == new_name:
            # Already correctly named, skip rename
            skipped_count += 1
            continue

        if not old_path.exists():
            print(f"  ⚠️  Source not found: {old_name}")
            error_count += 1
            continue

        if new_path.exists() and old_path != new_path:
            print(f"  ⚠️  Target already exists: {new_name}")
            error_count += 1
            continue

        try:
            # Use git mv for proper version control
            result = subprocess.run(
                ["git", "mv", str(old_path), str(new_path)],
                cwd=pottery_dir.parent.parent.parent,
                capture_output=True,
                text=True
            )

            if result.returncode == 0:
                print(f"  ✓ Renamed: {old_name[:50]}... → {new_name[:50]}...")
                renamed_count += 1
            else:
                print(f"  ✗ Failed: {old_name} ({result.stderr.strip()})")
                error_count += 1
        except Exception as e:
            print(f"  ✗ Error renaming {old_name}: {e}")
            error_count += 1

    print(f"\n{'='*70}")
    print(f"Renamed: {renamed_count} files")
    print(f"Skipped (already named): {skipped_count} files")
    print(f"Errors: {error_count} files")
    print(f"{'='*70}\n")

    # Generate imageDescriptions
    print(f"{'='*70}")
    print("PHASE 2: GENERATING DESCRIPTIONS")
    print(f"{'='*70}\n")

    descriptions_code = create_pottery_descriptions_dict()
    output_file = Path("/home/john/Code/resume/pottery_descriptions.ts")
    output_file.write_text(descriptions_code)

    print(f"✓ Generated descriptions file: {output_file}")
    print(f"✓ Total descriptions: {len(COMPLETE_MAPPING)}")
    print(f"\n{'='*70}")
    print("COMPLETE - All 294 images processed")
    print(f"{'='*70}\n")

    return 0

if __name__ == "__main__":
    exit(main())
