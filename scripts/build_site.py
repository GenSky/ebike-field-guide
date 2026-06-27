from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


MODELS = [
    {
        "slug": "aventon-level-3",
        "brand": "Aventon",
        "model": "Level.3",
        "category": "Best Overall / Commuter",
        "rating": "4.7",
        "price": "$1,899 MSRP, often discounted",
        "class": "Class 2 / configurable Class 3",
        "motor": "500W rear hub, torque sensor",
        "battery": "708Wh removable integrated pack",
        "range": "Up to about 70 miles claimed",
        "weight": "About 67 lb",
        "image": "https://cdn.shopify.com/s/files/1/1520/2468/files/01_Level.3_Matte-Aurora_Side_1-bike.jpg?v=1739400464",
        "official": "https://www.aventon.com/products/level-3-commuter-ebike",
        "source": "https://www.bicycling.com/bikes-gear/a70894696/aventon-level-3-e-bike-review/",
        "verdict": "The safest default recommendation for many first-time buyers because it combines commuter equipment, smooth assist, security tech, dealer availability, and fair pricing.",
        "best_for": "Daily commuters, errands, riders who want a complete bike rather than a project.",
        "avoid_if": "You need to carry the bike up stairs or want a light, analog-feeling ride.",
        "pros": ["Excellent equipment for the money", "Torque sensor and hydraulic brakes", "Rack, fenders, lights, turn signals, GPS/security features", "Large battery and broad shop presence"],
        "cons": ["Heavy", "Connected features may add subscription cost after the first year", "Direct-to-consumer assembly can still require tuning"],
    },
    {
        "slug": "ride1up-roadster-v3",
        "brand": "Ride1Up",
        "model": "Roadster V3",
        "category": "Best Budget Road / Fitness",
        "rating": "4.6",
        "price": "About $1,395",
        "class": "Configurable Class 1/2/3",
        "motor": "500W rear hub, torque sensor",
        "battery": "Removable pack, UL 2271 noted in reviews",
        "range": "Roughly 40-45+ miles depending on build and assist",
        "weight": "About 40 lb",
        "image": "https://ride1up.com/wp-content/uploads/2026/03/RV3-MedLrg_Grn-scaled.webp",
        "official": "https://ride1up.com/product/roadster-v3/",
        "source": "https://www.t3.com/active/cycling/ride1up-roadster-v3-review",
        "verdict": "A strong value pick if you want an e-bike that still feels close to a normal city or fitness bike.",
        "best_for": "Riders who value lower weight, speed, and a cleaner look over cargo capacity.",
        "avoid_if": "You need broad local dealer service or a plush upright cruiser.",
        "pros": ["Light by e-bike standards", "Natural torque-sensor feel", "Good price-to-spec ratio", "Belt or 9-speed drivetrain options"],
        "cons": ["Less cargo-ready than full commuters", "Direct-to-consumer support is not the same as a dealer network", "Basic throttle implementation"],
    },
    {
        "slug": "aventon-abound-lr",
        "brand": "Aventon",
        "model": "Abound LR",
        "category": "Best Cargo / Family Value",
        "rating": "4.5",
        "price": "About $1,999",
        "class": "Class 2 cargo e-bike",
        "motor": "750W rear hub, torque sensor",
        "battery": "733Wh removable pack",
        "range": "Up to about 60 miles claimed",
        "weight": "About 88 lb",
        "image": "https://cdn.shopify.com/s/files/1/1520/2468/files/01_Abound-LR_Stealth_Side_1-bike.jpg?v=1737999400",
        "official": "https://www.aventon.com/products/abound-lr-ebike",
        "source": "https://www.tomsguide.com/vehicle-tech/electric-bikes/aventon-abound-lr-review",
        "verdict": "The cargo pick for buyers who want real daily utility without jumping into premium cargo-bike pricing.",
        "best_for": "School runs, groceries, car-replacement errands, and one-bike households.",
        "avoid_if": "You live upstairs, have narrow storage, or do not need cargo capacity.",
        "pros": ["Strong value for a long-tail cargo bike", "Stable under load", "Passenger and utility accessory ecosystem", "Security features and integrated lighting"],
        "cons": ["Large and heavy", "Needs dedicated storage", "Accessory choices matter for passenger use"],
    },
    {
        "slug": "lectric-xp4-750",
        "brand": "Lectric",
        "model": "XP4 750",
        "category": "Best Budget Folding",
        "rating": "4.3",
        "price": "$999 base, more for 750/long-range configurations",
        "class": "Folding Class 2/3 capable",
        "motor": "750W rear hub on 750 build",
        "battery": "17.5Ah long-range option",
        "range": "Up to 85 miles claimed; 50+ miles reported in review use",
        "weight": "About 62 lb",
        "image": "https://media.wired.com/photos/690547ac162b6af54df5fedd/191:100/w_1280,c_limit/Review-%20Lectric%20XP4%20750%20Electric%20Bike.png",
        "official": "https://lectricebikes.com/",
        "source": "https://www.wired.com/review/lectric-xp4-750-electric-bike",
        "verdict": "A budget utility folder that makes sense when storage and price matter more than polish.",
        "best_for": "Apartments, RVs, trunk storage, and riders who want utility at a low price.",
        "avoid_if": "You expect a light folding bike you can casually carry one-handed.",
        "pros": ["Very aggressive pricing", "Folds for transport", "Strong range and power for the money", "Hydraulic brakes on reviewed build"],
        "cons": ["Still heavy when folded", "Fit can be awkward for very tall riders", "One-sided kickstand and folder compromises"],
    },
    {
        "slug": "urtopia-carbon-fold-2",
        "brand": "Urtopia",
        "model": "Carbon Fold 2",
        "category": "Best Premium Folding",
        "rating": "4.2",
        "price": "About $1,899",
        "class": "20 mph folding e-bike",
        "motor": "Peak 500W hub motor, 42Nm",
        "battery": "244.8Wh seatpost battery; optional extender",
        "range": "45 miles claimed, up to 95 with optional battery",
        "weight": "About 35 lb without accessories",
        "image": "https://cdn.mos.cms.futurecdn.net/udht5zmi8ZtQWcMGpUAesC-2048-80.jpg",
        "official": "https://newurtopia.com/",
        "source": "https://www.tomsguide.com/vehicle-tech/electric-bikes/urtopia-carbon-fold-2-more-refined",
        "verdict": "A lighter, more polished folder for small-space riders who can live with payload and folding-retention tradeoffs.",
        "best_for": "Apartment storage, trunk carry, lighter riders, and multimodal trips.",
        "avoid_if": "You need high payload capacity, kid/cargo duty, or a rock-solid folded latch.",
        "pros": ["Light for a folding e-bike", "Compact carbon-frame design", "Removable seatpost battery", "Optional extended range"],
        "cons": ["Payload limit is restrictive", "Folded retention can be weak", "Small battery unless upgraded"],
    },
    {
        "slug": "velotric-discover-2",
        "brand": "Velotric",
        "model": "Discover 2",
        "category": "Best Comfort Value",
        "rating": "4.4",
        "price": "Often around the mid-$1,000 range",
        "class": "Class 1/2/3 configurable",
        "motor": "750W rear hub, 75Nm",
        "battery": "705.6Wh removable pack",
        "range": "Up to 60 throttle / 75 pedal-assist miles claimed",
        "weight": "Heavy comfort commuter class",
        "image": "https://media.wired.com/photos/693c7360fd0148aae4721aa4/191:100/w_1280,c_limit/Review%20Velotric%20Discover%202%20Electric%20Bike%20top%20art%20122025%20SOURCE%20Velotric%20Bike.jpg",
        "official": "https://www.velotricbike.com/products/velotric-discover-2",
        "source": "https://www.wired.com/review/velotric-discover-2",
        "verdict": "A comfortable, powerful step-through with a lot of features for the money, especially for hilly urban routes.",
        "best_for": "Comfort-first commuting, hills, rough streets, and riders who want security features.",
        "avoid_if": "You want a simple locked-down Class 1 bike or a lightweight ride.",
        "pros": ["Powerful motor", "Large battery", "Turn signals, rack, lights, USB-C, Apple Find My support", "Torque/cadence sensor flexibility"],
        "cons": ["Class flexibility requires rule awareness", "Headlight criticism in high-speed dark riding", "Heavy"],
    },
    {
        "slug": "niu-bqi-c3-pro",
        "brand": "NIU",
        "model": "BQi-C3 Pro",
        "category": "Best Long Range",
        "rating": "4.1",
        "price": "Varies widely by retailer and sale",
        "class": "20 mph commuter e-bike",
        "motor": "500W rear hub, 750W max",
        "battery": "Dual 48V 20Ah removable batteries",
        "range": "Up to 90 miles claimed and supported by testing coverage",
        "weight": "About 70.5 lb",
        "image": "https://cdn.mos.cms.futurecdn.net/wf8LbpXFH4UjqQxB2kgc23-2000-80.jpg",
        "official": "https://www.niu.com/",
        "source": "https://www.tomsguide.com/best-picks/best-electric-bikes",
        "verdict": "The range-anxiety pick: heavy, but unusually practical for long errands or commutes where charging is inconvenient.",
        "best_for": "Long commutes, riders without workplace charging, and simple belt-drive commuting.",
        "avoid_if": "You need to lift the bike or want premium braking components.",
        "pros": ["Dual-battery range", "Belt drive", "Integrated lights and rack", "Step-through utility"],
        "cons": ["Very heavy for non-cargo use", "Mechanical brakes", "Less sporty than lighter commuters"],
    },
    {
        "slug": "aventon-aventure-2",
        "brand": "Aventon",
        "model": "Aventure.2",
        "category": "Best Fat-Tire / All-Terrain",
        "rating": "4.3",
        "price": "Often around $1,500-$2,000 depending on sale",
        "class": "Class 2, unlockable pedal assist where legal",
        "motor": "750W rear hub with torque sensing",
        "battery": "Large removable integrated pack",
        "range": "Varies by terrain; strong practical range in review use",
        "weight": "About 77 lb",
        "image": "https://media.wired.com/photos/64f23b56254f73cfa970574f/191:100/w_1280,c_limit/Aventon-Aventure.2-Featured-Gear.jpg",
        "official": "https://www.aventon.com/products/aventure-2-ebike",
        "source": "https://www.wired.com/review/aventon-aventure2",
        "verdict": "A fun, stable all-terrain e-bike that can commute during the week and explore rougher surfaces on weekends.",
        "best_for": "Gravel, parks, rough shoulders, heavier riders, and mixed-use households.",
        "avoid_if": "You mostly ride narrow bike rooms, transit, stairs, or dense city racks.",
        "pros": ["Stable fat tires", "Strong motor", "Useful integrated lights and rack", "Good one-bike versatility"],
        "cons": ["Big and heavy", "Overkill for smooth pavement", "Needs careful assembly/tuning"],
    },
    {
        "slug": "specialized-turbo-vado-5",
        "brand": "Specialized",
        "model": "Turbo Vado 5.0",
        "category": "Best Premium Commuter",
        "rating": "4.5",
        "price": "Premium dealer-bike pricing",
        "class": "Commuter / hybrid e-bike",
        "motor": "Specialized/Brose mid-drive platform",
        "battery": "Large integrated pack, model-year dependent",
        "range": "High commuter range; depends on generation and assist",
        "weight": "Premium hybrid e-bike class",
        "image": "https://cdn.mos.cms.futurecdn.net/6KUQcCvt6okX9NWEYkh3mk-2000-80.jpg",
        "official": "https://www.specialized.com/",
        "source": "https://www.techradar.com/best/electric-bike",
        "verdict": "A premium shop-supported commuter for people who want a refined ride, quality components, and dealer service.",
        "best_for": "Serious commuting, longer ownership, and riders who want local support.",
        "avoid_if": "You are shopping primarily on price or need throttle capability.",
        "pros": ["Smooth premium ride", "Dealer network", "Good component quality", "More polished than most value brands"],
        "cons": ["Expensive", "Less cargo-focused", "Model-year specs vary"],
    },
    {
        "slug": "gazelle-eclipse-c380",
        "brand": "Gazelle",
        "model": "Eclipse C380+",
        "category": "Best Luxury / Comfort",
        "rating": "4.4",
        "price": "Premium Dutch commuter pricing",
        "class": "Class 3 comfort commuter",
        "motor": "Bosch Performance Line, 85Nm",
        "battery": "750Wh integrated battery",
        "range": "Long practical commuter range",
        "weight": "About 62 lb in reviewed build",
        "image": "https://cloudinary.pondigital.solutions/pon-digital-solutions/image/upload/q_auto,f_auto/dmp.pon.bike/1280_E6GLelBLiMp29Iao.png",
        "official": "https://www.gazellebikes.com/en-us/gazelle-eclipse-c380plus-hmb",
        "source": "https://www.wired.com/review/gazelle-eclipse",
        "verdict": "A high-comfort luxury commuter with Bosch power, belt drive, and the details that make daily riding feel easy.",
        "best_for": "Comfort-first riders, longer commutes, low-maintenance drivetrain fans, premium buyers.",
        "avoid_if": "You need a budget bike, a throttle, or an easy bike to carry.",
        "pros": ["Bosch system", "Enviolo hub and belt drive", "Large battery", "Excellent comfort and finish"],
        "cons": ["Expensive", "Heavy", "More city/road focused than true trail capable"],
    },
]


CATEGORIES = [
    ("Best Overall", ["Aventon Level.3", "Velotric Discover 2", "Specialized Turbo Vado 5.0"], "Balanced picks that cover commuting, errands, comfort, and ownership support."),
    ("Best Budget", ["Lectric XP4 750", "Ride1Up Roadster V3", "Aventon Soltera.2"], "Lower-cost models that still have credible brakes, batteries, and everyday usability."),
    ("Best Commuter", ["Aventon Level.3", "Gazelle Medeo T9 City", "Trek Verve+ 3"], "Rack, fenders, lights, predictable handling, and enough range for daily trips."),
    ("Best Road / Fitness", ["Ride1Up Roadster V3", "Specialized Turbo Vado SL", "Trek Domane+ SLR"], "Lighter, faster, more bike-like e-bikes for riders who still want exercise."),
    ("Best Luxury", ["Gazelle Eclipse C380+", "Riese & Muller Charger4", "Specialized Turbo Vado 5.0"], "Premium systems, dealer support, belt drives, Bosch/Shimano motors, and polished fit."),
    ("Best Cargo / Family", ["Aventon Abound LR", "Tern HSD P5i", "Yuba Spicy Curry"], "Passenger kits, payload, kickstand stability, and accessory ecosystems matter most."),
    ("Best Folding", ["Lectric XP4 750", "Urtopia Carbon Fold 2", "Tern Vektron P5i"], "Storage and transport picks; weight still matters as much as folded size."),
    ("Best Fat-Tire / All-Terrain", ["Aventon Aventure.2", "Radster Trail", "Velotric Nomad"], "Stable big-tire bikes for rough pavement, gravel, snow, and casual dirt paths."),
    ("Best Long Range", ["NIU BQi-C3 Pro", "Urtopia Carbon Fold 2 Dual Battery", "Gazelle Eclipse C380+"], "Large or dual-battery bikes for riders who cannot charge often."),
    ("Best Trail / Mountain", ["Specialized Turbo Levo", "Trek Rail+", "Aventon Ramblas"], "Real trail geometry, suspension, brakes, and local trail legality."),
    ("Best Comfort / Seniors", ["Gazelle Ultimate C380", "Velotric Discover 2", "Aventon Pace"], "Low step-through frames, upright posture, gentle handling, and predictable assist."),
    ("Best Low Maintenance", ["Gazelle Eclipse C380+", "Priority Current Plus", "Tenways CGO600 Pro"], "Belt drives, internal hubs, proven systems, and fewer drivetrain chores."),
]


MANUFACTURERS = [
    ("Aventon", "Value commuters, cargo, fat tire, and smart-security features", "Level.3, Abound LR, Aventure.2, Pace"),
    ("Lectric", "Budget folding and utility e-bikes", "XP4, XPedition, XP Trike"),
    ("Ride1Up", "Value road, city, and commuter bikes", "Roadster V3, Portola, Prodigy"),
    ("Rad Power / Rad Life", "Utility, fat tire, and cargo heritage", "Radster, RadRunner, RadWagon"),
    ("Specialized", "Premium commuter, road, and mountain e-bikes", "Turbo Vado, Turbo Levo, Vado SL"),
    ("Trek", "Dealer-supported commuter, road, and trail", "Verve+, Domane+, Rail+"),
    ("Gazelle", "Dutch comfort commuters with Bosch systems", "Eclipse, Ultimate, Medeo"),
    ("Tern", "Compact cargo, folding, and family utility", "HSD, GSD, Vektron"),
    ("Riese & Muller", "Luxury cargo and touring e-bikes", "Charger4, Nevo4, Load"),
    ("Cannondale", "Shop-supported fitness, commuter, and e-MTB", "Synapse Neo, Moterra, Adventure Neo"),
    ("Giant / Liv", "Broad dealer-backed road, city, and mountain range", "Explore E+, Road E+, Trance X E+"),
    ("Santa Cruz", "Premium e-mountain bikes", "Heckler, Skitch"),
    ("Yuba", "Cargo and family bikes", "Spicy Curry, Mundo Electric"),
    ("Benno", "Compact cargo and utility", "Boost, RemiDemi"),
    ("Urban Arrow", "Front-loader family cargo", "Family, Cargo"),
    ("Brompton", "Premium compact folding", "Electric C Line, Electric G Line"),
    ("Gocycle", "Premium folding urban e-bikes", "G4, G4i"),
    ("Urtopia", "Lightweight smart city and folding bikes", "Carbon Fold 2, Carbon 1"),
    ("Velotric", "Comfort and value commuters", "Discover 2, Nomad, T1"),
    ("NIU", "Long-range and micromobility crossover", "BQi-C3 Pro"),
    ("Tenways", "Light belt-drive city e-bikes", "CGO600 Pro, AGO T"),
    ("Priority", "Belt-drive low-maintenance commuters", "Current Plus, E-Coast"),
    ("Vvolt", "Clean belt-drive city and commuter bikes", "Centauri, Alpha"),
    ("Co-op Cycles", "REI-backed value commuters", "CTY e-series"),
    ("Cube", "European trekking and e-MTB range", "Reaction Hybrid, Kathmandu Hybrid"),
    ("Canyon", "Direct-to-consumer road, gravel, and city e-bikes", "Pathlite:ON, Grail:ON"),
    ("Orbea", "Lightweight road, gravel, and e-MTB", "Gain, Rise, Diem"),
    ("Haibike", "Sport and e-mountain heritage", "AllMtn, Trekking"),
    ("Blix", "Utility, cruiser, and cargo", "Packa, Vika, Sol"),
    ("Mokwheel", "Fat-tire and outdoor utility", "Basalt, Obsidian"),
]


MANUFACTURER_URLS = {
    "Aventon": "https://www.aventon.com/",
    "Lectric": "https://lectricebikes.com/",
    "Ride1Up": "https://ride1up.com/",
    "Rad Power / Rad Life": "https://www.radpowerbikes.com/",
    "Specialized": "https://www.specialized.com/us/en",
    "Trek": "https://www.trekbikes.com/us/en_US/",
    "Gazelle": "https://www.gazellebikes.com/en-us",
    "Tern": "https://www.ternbicycles.com/us",
    "Riese & Muller": "https://www.r-m.de/en-us/",
    "Cannondale": "https://www.cannondale.com/en-us",
    "Giant / Liv": "https://www.giant-bicycles.com/us/bikes/electric-bikes",
    "Santa Cruz": "https://www.santacruzbicycles.com/en-US/bikes",
    "Yuba": "https://yubabikes.com/",
    "Benno": "https://bennobikes.com/",
    "Urban Arrow": "https://urbanarrow.com/",
    "Brompton": "https://us.brompton.com/c/electric-bikes",
    "Gocycle": "https://gocycle.com/",
    "Urtopia": "https://newurtopia.com/",
    "Velotric": "https://www.velotricbike.com/",
    "NIU": "https://www.niu.com/us",
    "Tenways": "https://us.tenways.com/",
    "Priority": "https://www.prioritybicycles.com/",
    "Vvolt": "https://vvolt.com/",
    "Co-op Cycles": "https://www.rei.com/b/co-op-cycles/c/electric-bikes",
    "Cube": "https://www.cube.eu/",
    "Canyon": "https://www.canyon.com/en-us/electric-bikes/",
    "Orbea": "https://www.orbea.com/us-en/ebikes/",
    "Haibike": "https://www.haibike.com/us/en",
    "Blix": "https://blixbike.com/",
    "Mokwheel": "https://www.mokwheel.com/",
}


SOURCES = [
    ("15 U.S.C. 2085 federal low-speed electric bicycle definition", "https://www.law.cornell.edu/uscode/text/15/2085"),
    ("CPSC bicycle requirements, 16 CFR Part 1512", "https://www.ecfr.gov/current/title-16/chapter-II/subchapter-C/part-1512"),
    ("NHTSA bicycle safety guidance", "https://www.nhtsa.gov/road-safety/bicycle-safety"),
    ("FDNY lithium-ion battery safety tips", "https://www.fdnysmart.org/be-fdnysmart-when-using-any-devices-powered-by-lithium-ion-batteries/"),
    ("UL 2849 electrical systems for eBikes", "https://www.shopulstandards.com/ProductDetail.aspx?productId=UL2849"),
    ("Tom's Guide 2026 tested e-bike roundup", "https://www.tomsguide.com/best-picks/best-electric-bikes"),
    ("Bicycling Aventon Level.3 review", "https://www.bicycling.com/bikes-gear/a70894696/aventon-level-3-e-bike-review/"),
    ("WIRED Lectric XP4 750 review", "https://www.wired.com/review/lectric-xp4-750-electric-bike"),
    ("WIRED Velotric Discover 2 review", "https://www.wired.com/review/velotric-discover-2"),
    ("Tom's Guide Urtopia Carbon Fold 2 review", "https://www.tomsguide.com/vehicle-tech/electric-bikes/urtopia-carbon-fold-2-more-refined"),
]


def stars(rating: str) -> str:
    value = float(rating)
    full = int(value)
    return "★" * full + "☆" * (5 - full)


def attrs(**kwargs):
    return " ".join(f'{k}="{escape(str(v), quote=True)}"' for k, v in kwargs.items() if v)


def layout(title, description, body, root_prefix=""):
    return f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="{escape(description, quote=True)}">
    <title>{escape(title)}</title>
    <link rel="stylesheet" href="{root_prefix}styles.css">
  </head>
  <body>
    <header class="site-header">
      <a class="brand" href="{root_prefix}index.html">
        <span class="brand-mark" aria-hidden="true">E</span>
        <span>E-Bike Review Index</span>
      </a>
      <nav>
        <a href="{root_prefix}index.html#categories">Categories</a>
        <a href="{root_prefix}index.html#top-picks">Top Picks</a>
        <a href="{root_prefix}index.html#manufacturers">Manufacturers</a>
        <a href="{root_prefix}index.html#sources">Sources</a>
      </nav>
    </header>
    {body.lstrip()}
  </body>
</html>
"""


def model_card(model, root_prefix=""):
    return f"""
          <article class="review-card">
            <a class="review-image" href="{root_prefix}reviews/{model['slug']}.html">
              <img src="{escape(model['image'], quote=True)}" alt="{escape(model['brand'] + ' ' + model['model'])}" loading="lazy">
            </a>
            <div class="review-body">
              <div class="review-meta">
                <span>{escape(model['category'])}</span>
                <strong>{stars(model['rating'])} {model['rating']}</strong>
              </div>
              <h3>{escape(model['brand'])} {escape(model['model'])}</h3>
              <p>{escape(model['verdict'])}</p>
              <dl class="mini-specs">
                <div><dt>Price</dt><dd>{escape(model['price'])}</dd></div>
                <div><dt>Range</dt><dd>{escape(model['range'])}</dd></div>
              </dl>
              <a class="text-link" href="{root_prefix}reviews/{model['slug']}.html">Read detailed review</a>
            </div>
          </article>"""


def build_index():
    top_cards = "\n".join(model_card(model) for model in MODELS[:6])
    more_cards = "\n".join(model_card(model) for model in MODELS[6:])
    category_cards = "\n".join(
        f"""
          <article class="category-card">
            <h3>{escape(name)}</h3>
            <p>{escape(summary)}</p>
            <ol>
              {''.join(f'<li>{escape(item)}</li>' for item in picks)}
            </ol>
          </article>"""
        for name, picks, summary in CATEGORIES
    )
    manufacturer_rows = "\n".join(
        f"""
          <tr>
            <th><a class="maker-link" href="{escape(MANUFACTURER_URLS[name], quote=True)}">{escape(name)}</a></th>
            <td>{escape(positioning)}</td>
            <td>{escape(models)}</td>
          </tr>"""
        for name, positioning, models in MANUFACTURERS
    )
    source_links = "\n".join(f'<a href="{escape(url, quote=True)}">{escape(label)}</a>' for label, url in SOURCES)
    body = f"""
    <main id="top">
      <section class="review-hero">
        <div class="review-hero-media">
          <img src="assets/hero-ebike.png" alt="Modern electric bicycle on a city route">
        </div>
        <div class="review-hero-content">
          <p class="eyebrow">2026 buyer-oriented review hub</p>
          <h1>E-Bike Review Index</h1>
          <p class="lede">A category-first map of e-bike manufacturers and models, with quick reviews, estimated star ratings, specs, images, and deeper model pages.</p>
          <div class="hero-actions">
            <a class="button primary" href="#categories">Browse categories</a>
            <a class="button secondary" href="#top-picks">See top picks</a>
          </div>
        </div>
      </section>

      <section class="quick-stats">
        <div><strong>30</strong><span>manufacturers mapped</span></div>
        <div><strong>12</strong><span>shopping categories</span></div>
        <div><strong>10</strong><span>detailed model reviews</span></div>
      </section>

      <section id="categories" class="section">
        <div class="section-heading">
          <p class="eyebrow">Start by use case</p>
          <h2>Categories make the market easier to compare.</h2>
          <p>Most buyers should choose a category first, then compare two or three models inside that category. A great cargo bike can be a poor apartment bike; a great road e-bike can be the wrong grocery hauler.</p>
        </div>
        <div class="category-grid">{category_cards}
        </div>
      </section>

      <section id="top-picks" class="section review-band">
        <div class="section-heading">
          <p class="eyebrow">Detailed reviews</p>
          <h2>Top models with photos, verdicts, and tradeoffs.</h2>
          <p>Ratings are field-guide estimates that combine published testing, specs, safety posture, fit for category, service practicality, and value.</p>
        </div>
        <div class="review-grid">{top_cards}
        </div>
      </section>

      <section class="section">
        <div class="section-heading">
          <p class="eyebrow">More strong contenders</p>
          <h2>Specialized picks for range, terrain, and premium comfort.</h2>
        </div>
        <div class="review-grid">{more_cards}
        </div>
      </section>

      <section id="manufacturers" class="section">
        <div class="section-heading">
          <p class="eyebrow">Manufacturer directory</p>
          <h2>Who makes e-bikes, and where they fit.</h2>
          <p>This directory is intentionally broad: value direct-to-consumer brands, dealer-supported bike companies, cargo specialists, Dutch comfort brands, and premium e-MTB makers.</p>
        </div>
        <div class="table-wrap">
          <table class="maker-table">
            <thead>
              <tr><th>Manufacturer</th><th>Where they fit</th><th>Models to know</th></tr>
            </thead>
            <tbody>{manufacturer_rows}
            </tbody>
          </table>
        </div>
      </section>

      <section id="safety" class="section safety-band">
        <div class="section-heading">
          <p class="eyebrow">Review criteria</p>
          <h2>How the ratings are weighted.</h2>
        </div>
        <div class="criteria-grid">
          <article><h3>Category fit</h3><p>Does the bike do the job the buyer is hiring it for?</p></article>
          <article><h3>Safety posture</h3><p>Brakes, battery certification claims, lighting, handling, and legal class clarity.</p></article>
          <article><h3>Ownership</h3><p>Service network, parts availability, accessories, warranty, and storage reality.</p></article>
          <article><h3>Value</h3><p>What the buyer gets after accounting for required accessories and likely discounts.</p></article>
        </div>
      </section>

      <section id="sources" class="section sources-section">
        <div class="section-heading">
          <p class="eyebrow">Sources</p>
          <h2>Research links used for the review hub.</h2>
        </div>
        <div class="source-list">{source_links}</div>
      </section>
    </main>
    <footer class="site-footer">
      <p>E-Bike Review Index</p>
      <a href="#top">Back to top</a>
    </footer>
"""
    return layout("E-Bike Review Index", "Review-focused e-bike category guide with manufacturers, ratings, images, and detailed model pages.", body)


def build_review(model):
    related = [m for m in MODELS if m["slug"] != model["slug"] and (m["category"].split("/")[0].strip() in model["category"] or model["brand"] == m["brand"])][:3]
    if len(related) < 3:
        related = (related + [m for m in MODELS if m["slug"] != model["slug"]])[:3]
    related_cards = "\n".join(model_card(m, "../") for m in related)
    spec_rows = "".join(
        f"<tr><th>{escape(label)}</th><td>{escape(model[key])}</td></tr>"
        for label, key in [
            ("Category", "category"),
            ("Estimated rating", "rating"),
            ("Price", "price"),
            ("Class", "class"),
            ("Motor", "motor"),
            ("Battery", "battery"),
            ("Range", "range"),
            ("Weight", "weight"),
        ]
    )
    body = f"""
    <main id="top">
      <section class="detail-hero">
        <div class="detail-copy">
          <p class="eyebrow">{escape(model['category'])}</p>
          <h1>{escape(model['brand'])} {escape(model['model'])}</h1>
          <p class="lede">{escape(model['verdict'])}</p>
          <div class="score-line">
            <strong>{stars(model['rating'])} {model['rating']} / 5</strong>
            <span>Field-guide estimate, June 2026</span>
          </div>
          <div class="hero-actions">
            <a class="button primary" href="{escape(model['official'], quote=True)}">Official page</a>
            <a class="button secondary" href="{escape(model['source'], quote=True)}">Review source</a>
          </div>
        </div>
        <figure class="detail-media">
          <img src="{escape(model['image'], quote=True)}" alt="{escape(model['brand'] + ' ' + model['model'])}">
          <figcaption>Product/review image from linked manufacturer or review source.</figcaption>
        </figure>
      </section>

      <section class="section detail-section">
        <div class="detail-grid">
          <article class="verdict-card">
            <h2>Quick review</h2>
            <p>{escape(model['verdict'])}</p>
            <p><strong>Best for:</strong> {escape(model['best_for'])}</p>
            <p><strong>Avoid if:</strong> {escape(model['avoid_if'])}</p>
          </article>
          <article class="verdict-card">
            <h2>What stands out</h2>
            <ul>{''.join(f'<li>{escape(item)}</li>' for item in model['pros'])}</ul>
          </article>
          <article class="verdict-card">
            <h2>Tradeoffs</h2>
            <ul>{''.join(f'<li>{escape(item)}</li>' for item in model['cons'])}</ul>
          </article>
        </div>
      </section>

      <section class="section">
        <div class="section-heading">
          <p class="eyebrow">Specs snapshot</p>
          <h2>The numbers to verify before purchase.</h2>
        </div>
        <div class="table-wrap">
          <table class="maker-table spec-table">
            <tbody>{spec_rows}</tbody>
          </table>
        </div>
      </section>

      <section class="section review-band">
        <div class="section-heading">
          <p class="eyebrow">Compare next</p>
          <h2>Similar models worth checking.</h2>
        </div>
        <div class="review-grid">{related_cards}</div>
      </section>
    </main>
    <footer class="site-footer">
      <p><a href="../index.html">E-Bike Review Index</a></p>
      <a href="#top">Back to top</a>
    </footer>
"""
    return layout(f"{model['brand']} {model['model']} Review", model["verdict"], body, "../")


def main():
    (ROOT / "reviews").mkdir(exist_ok=True)
    (ROOT / "index.html").write_text(build_index(), encoding="utf-8")
    for model in MODELS:
        (ROOT / "reviews" / f"{model['slug']}.html").write_text(build_review(model), encoding="utf-8")


if __name__ == "__main__":
    main()
