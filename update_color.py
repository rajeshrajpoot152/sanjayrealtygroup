import glob

for file in glob.glob("*.html"):
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    # The user wants the 'footer-wave-dark' to have the same color as the footer bg (#001603)
    # So we replace %230F172A with %23001603 in the SVG for footer-wave-dark
    if "'footer-wave-dark': \"url('data:image/svg+xml,%3Csvg viewBox=\\\"0 0 1440 100\\\" xmlns=\\\"http://www.w3.org/2000/svg\\\" preserveAspectRatio=\\\"none\\\"%3E%3Cpath d=\\\"M0,0 C480,100 960,100 1440,0 L1440,100 L0,100 Z\\\" fill=\\\"%230F172A\\\"/%3E%3C/svg%3E')\"," in content:
        content = content.replace(
            "'footer-wave-dark': \"url('data:image/svg+xml,%3Csvg viewBox=\\\"0 0 1440 100\\\" xmlns=\\\"http://www.w3.org/2000/svg\\\" preserveAspectRatio=\\\"none\\\"%3E%3Cpath d=\\\"M0,0 C480,100 960,100 1440,0 L1440,100 L0,100 Z\\\" fill=\\\"%230F172A\\\"/%3E%3C/svg%3E')\",",
            "'footer-wave-dark': \"url('data:image/svg+xml,%3Csvg viewBox=\\\"0 0 1440 100\\\" xmlns=\\\"http://www.w3.org/2000/svg\\\" preserveAspectRatio=\\\"none\\\"%3E%3Cpath d=\\\"M0,0 C480,100 960,100 1440,0 L1440,100 L0,100 Z\\\" fill=\\\"%23001603\\\"/%3E%3C/svg%3E')\","
        )

    with open(file, "w", encoding="utf-8") as f:
        f.write(content)

print("Color updated")
