#!/usr/bin/env python3
"""Generate all Kuka illustrations for chapters 11-24 via pixazo-gen (Flux Schnell).
Idempotent: skips files that already exist. Run: python3 tools/generate-ilustrasi.py [N ...]
Optionally pass chapter numbers to limit."""
import os, subprocess, sys

PIXAZO = os.path.expanduser("~/.agents/bin/pixazo-gen.py")
BASE = "public/assets/illustrations"

HEADER = ("16:9 horizontal hand-drawn minimalist illustration, pure white background, "
          "black ink line art slightly wobbly, no shadows no gradients no textures except "
          "one soft elliptical shadow under the floating creature, no text no letters no "
          "words no numbers no labels no title no writing of any kind. ")
CREATURE = ("A small round soft-white bean-shaped creature with EXACTLY ONE single small solid "
            "dark circular eye (only one lens contains the eye, the other lens stays empty), "
            "the single eye peeking above thin round dark-framed eyeglasses, a crew-cut "
            "flat-top short dark hair patch on its head, two short stubby arms, no legs, "
            "hovering above a soft elliptical shadow, friendly curious slightly confused "
            "expression. ")
FOOTER = " Lots of empty white space. Strange but clean, not cute, not mascot, not children's cartoon, not PPT infographic."

# (chapter_dir, filename, use_creature, scene)
JOBS = [
    ("11-search", "01-katalog.png", True,
     "The creature opens one drawer of a huge library card catalog cabinet, tall bookshelves far in the background."),
    ("11-search", "02-inverted.png", True,
     "One large catalog card mounted on a wall with three connecting lines pointing to three different books on a shelf."),
    ("11-search", "03-fuzzy.png", True,
     "The creature hands over a catalog card that has one wobbly wrong stroke on it, a small clerk machine nods and accepts the card."),
    ("12-error", "01-jaring.png", True,
     "The creature stands beside a tall shelf with a large safety net stretched below it, one falling plate is caught mid-air by the net."),
    ("12-error", "02-health.png", True,
     "A small manager machine with a tall hat tastes from one big cooking pot while holding a small board with a single check mark."),
    ("12-error", "03-sapu.png", True,
     "The creature calmly sweeps up broken plate shards with a small broom, other pots keep steaming in the background."),
    ("13-grpc", "01-telepon.png", True,
     "Two kitchen desks face each other far apart; the creature talks into a desk telephone at the left desk, a straight telephone line connects both desks, a thick closed codebook lies open at the creature's desk."),
    ("13-grpc", "02-protokol.png", False,
     "Two identical thick codebooks with the same plain cover mark stand open on two desks facing each other across the scene."),
    ("13-grpc", "03-deadline.png", True,
     "The creature talks on the telephone while pointing at one big wall clock whose sand hourglass below is almost empty."),
    ("14-config", "01-panduan.png", True,
     "The creature reads one big open guidebook hanging on the kitchen wall, small neat sticky notes arranged in rows beside it."),
    ("14-config", "02-tempelan.png", True,
     "A wall covered in crooked scattered sticky notes tilted in every direction; the creature hovers in front of it looking confused."),
    ("14-config", "03-kunci.png", True,
     "The creature drops one small key into a small closed lockbox while the sticky note board behind stays empty of keys."),
    ("15-logging", "01-buku-harian.png", True,
     "The creature writes one line in a thick open daily logbook on the kitchen desk, a small wall panel with one rising line chart hangs beside it."),
    ("15-logging", "02-papan.png", True,
     "A wall board with three round gauges and one rising line chart; the creature glances at it while carrying plates."),
    ("15-logging", "03-tiket.png", True,
     "One paper ticket with a small clipped note travels desk to desk, dashed lines connect the desks in sequence, the creature watches the ticket pass."),
    ("16-shutdown", "01-papan.png", True,
     "The creature hangs one small blank closing board on the restaurant door while inside a waiter machine still serves seated guests."),
    ("16-shutdown", "02-draining.png", True,
     "Two tables of guests with plates remain while the waiter machine carries the last plate to one of them; the door behind is half closed."),
    ("16-shutdown", "03-beres-beres.png", True,
     "The creature washes the last pot in a washing basin, the shelf beside it is already empty and tidy."),
    ("17-security", "01-gembok.png", True,
     "The building door has three layers of security in a row: a padlock, a card reader, and a guard machine; the creature passes the first layer."),
    ("17-security", "02-sandi.png", True,
     "An open book shows pages of irregular unreadable scribble patterns; the creature closes one clean blank page over it."),
    ("17-security", "03-injection.png", True,
     "The creature hands one note to a receiving machine that has two separate slots, one marked with a simple command shape and one with a note shape, and the machine routes the note into the note slot only."),
    ("18-scaling1", "01-papan-angka.png", True,
     "The creature stands before a wall board with three round gauges and one line chart, pointing at the fullest gauge."),
    ("18-scaling1", "02-n-plus-1.png", True,
     "A waiter machine runs back and forth on a path between the kitchen and a table three times, each trip carrying one tiny ingredient."),
    ("18-scaling1", "03-load-balancer.png", True,
     "A receptionist machine divides three arriving guests equally toward three empty tables at equal distances."),
    ("19-scaling2", "01-cabang.png", True,
     "Three identical twin restaurant buildings stand in a row, each with the same small board; the creature hovers in front of the middle building."),
    ("19-scaling2", "02-sharding.png", True,
     "One thick ledger book splits into two thinner books; the creature holds one of the thin books."),
    ("19-scaling2", "03-cdn.png", True,
     "One central cabinet and three small racks in three different corners hold the same jars; dashed lines connect the cabinet to each rack."),
    ("20-concurrency", "01-dua-panci.png", True,
     "The creature stirs one pot while its other arm points at two more pots boiling beside it, each pot with a tiny bell on its lid."),
    ("20-concurrency", "02-paralel.png", False,
     "Three identical twin chef machines stir three separate pots on three separate stoves at the same time, in one straight row."),
    ("20-concurrency", "03-gula.png", True,
     "Two arms pour from two sugar shells into the same single pot at the same moment, the streams collide and spill."),
    ("21-container", "01-peti.png", True,
     "The creature stands beside one big closed crate decorated with simple stove and pot marks, a stack of identical crates behind it."),
    ("21-container", "02-manajer.png", False,
     "A one-eyed manager machine stands on a small stage watching five identical closed crates arranged in a tidy row below."),
    ("21-container", "03-pipeline.png", False,
     "Three desks in a row: a recipe desk, a crate assembly desk, and a shipping desk; one small crate moves between them along a conveyor."),
    ("22-testing", "01-uji-rasa.png", True,
     "The creature tastes from a tiny spoon in front of many small bowls arranged in a row, thinking expression."),
    ("22-testing", "02-piramida.png", False,
     "Small bowls stacked into a pyramid shape: many bowls at the bottom, fewer in the middle, exactly one bowl on top."),
    ("22-testing", "03-flaky.png", True,
     "One bowl drawn with two different taste-spoon marks on its two sides; the creature shakes its head at it."),
    ("23-kafka", "01-papan-log.png", True,
     "A huge board covered with a long dense column of numbered paper slips running top to bottom, none missing; the creature reads from the top slip."),
    ("23-kafka", "02-offset.png", False,
     "Three small chef machines stand at the same huge slip board, each holding its own bookmark at a different height."),
    ("23-kafka", "03-jalur.png", False,
     "One board with three separate slip lanes side by side, numbered slips flowing downward in order in each lane."),
    ("24-websocket", "01-pelayan-menetap.png", True,
     "A waiter machine stands right beside the creature's cafe table; the two face each other with a two-headed whisper line between them."),
    ("24-websocket", "02-handshake.png", True,
     "The creature holds out one card to a waiter machine at the door; the waiter nods and the door swings wide open."),
    ("24-websocket", "03-broadcast.png", False,
     "One waiter machine in the middle of the room hands plates out to four tables at once through branching dashed lines."),
]

def prompt_for(use_creature, scene):
    body = (HEADER + (CREATURE if use_creature else "") + scene + FOOTER)
    return body

def main():
    args = [int(a) for a in sys.argv[1:]]
    done = fail = skip = 0
    for ch_dir, fname, use_creature, scene in JOBS:
        chap = int(ch_dir.split("-")[0])
        if args and chap not in args:
            continue
        out = os.path.join(BASE, ch_dir, fname)
        if os.path.exists(out):
            skip += 1
            continue
        os.makedirs(os.path.dirname(out), exist_ok=True)
        r = subprocess.run(
            [sys.executable, PIXAZO, "-m", "flux-schnell", "-r", "16:9", "-s", "1600x900",
             "-o", out, prompt_for(use_creature, scene)],
            capture_output=True, text=True)
        if r.returncode == 0 and os.path.exists(out) and os.path.getsize(out) > 10000:
            done += 1
            print(f"OK   {out}")
        else:
            fail += 1
            print(f"FAIL {out}\n{r.stdout[-300:]}\n{r.stderr[-300:]}")
    print(f"\nSelesai: {done} baru, {skip} skip, {fail} gagal")

if __name__ == "__main__":
    main()
