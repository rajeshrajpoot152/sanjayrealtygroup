import glob
import re

before_classes_str = "before:absolute before:left-0 before:bottom-full before:w-full before:h-[70px] before:content-[''] before:z-10 before:bg-[url('data:image/svg+xml,%3Csvg_viewBox=%270_0_1440_100%27_xmlns=%27http://www.w3.org/2000/svg%27_preserveAspectRatio=%27none%27%3E%3Cpath_d=%27M0,0_C480,100_960,100_1440,0_L1440,100_L0,100_Z%27_fill=%27%230F172A%27/%3E%3C/svg%3E')] before:bg-[length:100%_100%] before:bg-no-repeat"
before_classes = before_classes_str.split()

def add_before(match):
    class_str = match.group(1)
    classes = class_str.split()
    
    if "footer" in classes:
        for bc in before_classes:
            if bc not in classes:
                classes.append(bc)
                
    return 'class="' + ' '.join(classes) + '"'

for file in glob.glob("*.html"):
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    content = re.sub(r'class="([^"]*)"', add_before, content)
    
    with open(file, "w", encoding="utf-8") as f:
        f.write(content)

print("Done")
