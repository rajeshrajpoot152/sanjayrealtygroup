import json
import re

testimonials = [
    {'name': 'Surinder Kumar', 'text': 'We purchased a prime location Propery in gift city through Sanjay Realty Group. We believe they are the best helpful and most friendly for any kind of property dealing in gift city, Gandhi nagar. Specially Ms. Rima Doshi has been very professional throughout our dealings. We highly recommend this firm to purchase property in gift city.'},
    {'name': 'Chetan Jalan', 'text': 'I am recommending Sanjay Realty Group after buying multiple properties from them. They are highly professional and reliable real estate advisors. They have great market insight and seamless service throughout the process. Thank you Sanjay Realty Group, GIFT city!!'},
    {'name': 'Bhavnish Shah', 'text': 'Booked 3 flats through Sanjay Realty Group in Gift City. They are honest, clear and helpful. I would recommend them to anyone looking to buy property. I had a great experience working with them.'},
    {'name': 'Palak Maithia', 'text': 'A true professional who made buying our property in GIFT city stress-free and exciting. Guided me through every step, ensuring transparency and satisfaction.'},
    {'name': 'Chinkal Parmar', 'text': 'Purchased the apartment in GIFT City through Sanjay Realty Group. Got the best deal. Knowledgeable and professional real estate agents for GIFT City, Gandhinagar area.'},
    {'name': 'Vrushant Panchal', 'text': 'If u r a investor in gandhinagar gift city this is the place to be. they will help u to buy sell or rent any property in gift city. very professional approach towards clients, they guide u in a right direction to buy property. a legit place to be to buy or sell or rent a property.'},
    {'name': 'Jigar Shukal', 'text': 'We purchased a prime location Property in adani santigram and gift city through Sanjay Realty Group. We believe they are the best helpful and most friendly for any kind of property dealing in gift city, Gandhi nagar. Specially Mr.Nitesh trivedi has been very professional throughout our dealings. We highly recommend this firm to purchase property in gift city.'},
    {'name': 'Prakash Patel', 'text': 'Sanjay Realty Group owner always very cooperative and giving best response as well as good rate on purchase.'},
    {'name': 'Rahul Singh, Pixielit Studios', 'text': 'Thanks for securing fully furnished office space for rent in Ahmedabad for my IT Startup. I was a first time business owner who is completely unaware to the leasing process and your experienced leasing agents handled the job with utmost Transparency and Professionalism which made the process seem easy.'},
    {'name': 'Sankalp Bhalla, Reliance General Insurance', 'text': 'It was indeed good experience to have the guidance and assistance of these guys, who knows the commercial property market in Ahmedabad very well, pays attention to understand the details of the business needs and provide incredible services.'},
    {'name': 'Riddhi Patel & Jatin Patel', 'text': 'We wanted to thank your marketing team for their excellent work in marketing our Commercial office Space in Ahmedabad. Within 60 days of enrollment with you there were multiple inquiries, including decent offers that culminated in a lease contract with a reputed MNC.'},
    {'name': 'Nirav Shah, House of Packaging', 'text': 'After checking with all my business and real estate connections, I choose Sanjay Realty Group to list my office in the Corporate Park. Within over a month period they were able to successfully rent out my commercial property to reputed corporate company for 3 year lease contract. I would say they are the best commercial real estate agents in Ahmedabad.'},
]

def get_initials(name):
    parts = name.split(',')[0].split(' ')
    return ''.join([p[0] for p in parts if p]).upper()[:2]

star_svg = '<svg width="16" height="16" viewBox="0 0 24 24" fill="#f59e0b" aria-hidden="true"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path></svg>'
stars = f'<div class="flex gap-0.5" role="img" aria-label="5 out of 5 stars">{star_svg * 5}</div>'

gradients = [
    'linear-gradient(135deg, #10b981 0%, #059669 100%)',
    'linear-gradient(135deg, #8b5cf6 0%, #ec4899 100%)',
    'linear-gradient(135deg, #06b6d4 0%, #3E96E4 100%)',
    'linear-gradient(135deg, #f97316 0%, #facc15 100%)',
    'linear-gradient(135deg, #3E96E4 0%, #0FC26A 100%)',
    'linear-gradient(135deg, #0F172A 0%, #D4AF37 100%)'
]

def create_card(t, idx):
    grad = gradients[idx % len(gradients)]
    return f'''<article class="bg-white border border-[#e2e8f0] rounded-2xl p-6 flex flex-col gap-4 w-full max-w-none shadow-sm">
    {stars}
    <p class="text-[14px] sm:text-[15px] text-[#374151] leading-relaxed">"{t['text']}"</p>
    <div class="flex items-center gap-3 mt-auto pt-2 border-t border-[#f1f5f9]">
        <div class="h-10 w-10 rounded-full flex items-center justify-center text-white text-[15px] font-bold shrink-0 ring-2 ring-white" style="background-image:{grad}" aria-hidden="true">{get_initials(t['name'])}</div>
        <div class="min-w-0">
            <p class="font-semibold text-[14px] text-[#0f172b] truncate">{t['name']}</p>
            <p class="text-[13px] text-[#6b7280] truncate">Happy Client</p>
        </div>
    </div>
</article>'''

# We divide into 3 columns
col1 = testimonials[0:4]
col2 = testimonials[4:8]
col3 = testimonials[8:12]

# To make it loop seamlessly, we duplicate each list twice so it overflows the height smoothly.
col1_html = ''.join([create_card(t, i) for i, t in enumerate(col1 + col1)])
col2_html = ''.join([create_card(t, i+4) for i, t in enumerate(col2 + col2)])
col3_html = ''.join([create_card(t, i+8) for i, t in enumerate(col3 + col3)])

new_section = f'''    <!-- Client Testimonials Section -->
    <section class="py-24 bg-brand-gray overflow-hidden">
        <style>
            @keyframes scroll-vertical {{
                from {{ transform: translateY(0); }}
                to {{ transform: translateY(-50%); }}
            }}
            @keyframes scroll-vertical-reverse {{
                from {{ transform: translateY(-50%); }}
                to {{ transform: translateY(0); }}
            }}
            .testimonials-scroll {{
                animation: scroll-vertical 40s linear infinite;
            }}
            .testimonials-scroll-reverse {{
                animation: scroll-vertical-reverse 40s linear infinite;
            }}
            .testimonials-scroll:hover, .testimonials-scroll-reverse:hover {{
                animation-play-state: paused;
            }}
        </style>
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mb-4 text-center reveal">
            <span class="inline-block bg-brand-gold/10 text-brand-gold text-xs font-bold uppercase tracking-widest px-4 py-1.5 rounded-full mb-4">Client Success Stories</span>
            <h2 class="font-heading text-4xl md:text-5xl font-bold text-brand-navy mb-4">What Our Clients Say</h2>
            <p class="text-gray-600 max-w-2xl mx-auto text-lg">Read about the experiences of our valued clients and how we've helped them secure prime real estate and commercial properties.</p>
        </div>

        <div class="flex justify-center gap-5 mt-10 sm:mt-12 [mask-image:linear-gradient(to_bottom,transparent,black_12%,black_88%,transparent)] max-h-[740px] overflow-hidden max-w-7xl mx-auto px-4">
            <!-- Column 1 -->
            <div class="flex-1 max-w-[420px]">
                <div class="testimonials-scroll flex flex-col gap-5 pb-5">
                    {col1_html}
                </div>
            </div>
            
            <!-- Column 2 (Hidden on Mobile) -->
            <div class="hidden md:block flex-1 max-w-[420px]">
                <div class="testimonials-scroll-reverse flex flex-col gap-5 pb-5">
                    {col2_html}
                </div>
            </div>
            
            <!-- Column 3 (Hidden on Mobile/Tablet) -->
            <div class="hidden lg:block flex-1 max-w-[420px]">
                <div class="testimonials-scroll flex flex-col gap-5 pb-5">
                    {col3_html}
                </div>
            </div>
        </div>
    </section>'''

import glob
import os

def update_html_files():
    for filepath in glob.glob("*.html"):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # The section we want to replace starts at <!-- Client Testimonials Section --> and ends at </section>
        pattern = r'<!-- Client Testimonials Section -->\s*<section.*?</section>'
        new_content = re.sub(pattern, new_section, content, flags=re.DOTALL)
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated testimonials in {filepath}")

update_html_files()
print("All done!")
