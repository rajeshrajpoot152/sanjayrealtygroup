import glob
import re

footer_wave_dark = "'footer-wave-dark': \"url('data:image/svg+xml,%3Csvg viewBox=\\\"0 0 1440 100\\\" xmlns=\\\"http://www.w3.org/2000/svg\\\" preserveAspectRatio=\\\"none\\\"%3E%3Cpath d=\\\"M0,0 C480,100 960,100 1440,0 L1440,100 L0,100 Z\\\" fill=\\\"%230F172A\\\"/%3E%3C/svg%3E')\","
footer_wave_green = "'footer-wave-green': \"url('data:image/svg+xml,%3Csvg viewBox=\\\"0 0 1440 100\\\" xmlns=\\\"http://www.w3.org/2000/svg\\\" preserveAspectRatio=\\\"none\\\"%3E%3Cpath d=\\\"M0,0 C480,100 960,100 1440,0 L1440,100 L0,100 Z\\\" fill=\\\"%23001603\\\"/%3E%3C/svg%3E')\","

for file in glob.glob("*.html"):
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update tailwind.config backgroundImage
    if "'footer-wave-dark'" not in content:
        # find backgroundImage: { and insert our waves
        pattern = r"(backgroundImage:\s*\{)"
        replacement = r"\1\n                        " + footer_wave_dark + r"\n                        " + footer_wave_green
        content = re.sub(pattern, replacement, content)

    # 2. Update footer classes
    # We want to replace the crazy arbitrary url classes with the new named utility classes
    def update_footer_classes(match):
        class_str = match.group(1)
        # Regex to remove the big before:bg-[...] and after:bg-[...]
        class_str = re.sub(r"before:bg-\[url\('[^']+'\)\]", "before:bg-footer-wave-dark", class_str)
        class_str = re.sub(r"after:bg-\[url\('[^']+'\)\]", "after:bg-footer-wave-green", class_str)
        return 'class="' + class_str + '"'

    content = re.sub(r'class="([^"]*footer[^"]*)"', update_footer_classes, content)

    with open(file, "w", encoding="utf-8") as f:
        f.write(content)

print("Done")
