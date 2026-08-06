import glob
import re

mapping = {
    "glass-nav": "bg-slate-900/85 backdrop-blur-[12px] border-b border-white/10",
    "glass-card": "bg-white/95 backdrop-blur-[10px] border border-white/20 shadow-[0_8px_32px_0_rgba(0,0,0,0.05)]",
    "hover-lift": "transition-all duration-300 ease-[cubic-bezier(0.4,0,0.2,1)] hover:-translate-y-2 hover:shadow-[0_20px_40px_-10px_rgba(0,0,0,0.15)]",
    "text-gradient": "bg-gradient-to-r from-[#D4AF37] to-[#F3E5AB] bg-clip-text text-transparent",
    "hide-scrollbar": "[&::-webkit-scrollbar]:hidden [-ms-overflow-style:none] [scrollbar-width:none]",
    "reveal": "reveal opacity-0 translate-y-[30px] transition-all duration-[800ms] ease-out [&.active]:opacity-100 [&.active]:translate-y-0",
    "footer-wave": "relative before:absolute before:left-0 before:bottom-full before:w-full before:h-[70px] before:content-[''] before:z-10 before:bg-[url('data:image/svg+xml,%3Csvg_viewBox=%270_0_1440_100%27_xmlns=%27http://www.w3.org/2000/svg%27_preserveAspectRatio=%27none%27%3E%3Cpath_d=%27M0,0_C480,100_960,100_1440,0_L1440,100_L0,100_Z%27_fill=%27%230F172A%27/%3E%3C/svg%3E')] before:bg-[length:100%_100%] before:bg-no-repeat",
}

footer_classes = "relative after:absolute after:left-0 after:bottom-full after:w-full after:h-[70px] after:content-[''] after:z-[-1] after:bg-[url('data:image/svg+xml,%3Csvg_viewBox=%270_0_1440_100%27_xmlns=%27http://www.w3.org/2000/svg%27_preserveAspectRatio=%27none%27%3E%3Cpath_d=%27M0,0_C480,100_960,100_1440,0_L1440,100_L0,100_Z%27_fill=%27%23001603%27/%3E%3C/svg%3E')] after:bg-[length:100%_100%] after:bg-no-repeat".split()

def update_class(match):
    class_str = match.group(1)
    classes = class_str.split()
    new_classes = []
    has_footer = "footer" in classes
    
    for c in classes:
        # Prevent double adding if script is rerun
        if c in ["opacity-0", "translate-y-[30px]"]: continue 
        if c in mapping:
            new_classes.extend(mapping[c].split())
        else:
            new_classes.append(c)
            
    if has_footer:
        for fc in footer_classes:
            if fc not in new_classes:
                new_classes.append(fc)
                
    # Deduplicate keeping order
    seen = set()
    deduped = []
    for cls in new_classes:
        if cls not in seen:
            seen.add(cls)
            deduped.append(cls)
            
    return 'class="' + ' '.join(deduped) + '"'

for file in glob.glob("*.html"):
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Remove the <style> blocks
    content = re.sub(r'<style>\s*/\* Custom Styles.*?</style>', '', content, flags=re.DOTALL)
    content = re.sub(r'<style>\s*\.footer::after.*?</style>', '', content, flags=re.DOTALL)
    
    # Also if there are any other style tags that got missed because they don't have exactly those comments
    content = re.sub(r'<style>[^<]*\.glass-nav[^<]*</style>', '', content, flags=re.DOTALL)
    content = re.sub(r'<style>[^<]*\.footer-wave[^<]*</style>', '', content, flags=re.DOTALL)
    
    # Process classes
    content = re.sub(r'class="([^"]*)"', update_class, content)
    
    with open(file, "w", encoding="utf-8") as f:
        f.write(content)

print("Done")
