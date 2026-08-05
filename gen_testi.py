import json

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

star_svg = '<svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path></svg>'
stars = f'<div class="flex items-center gap-1 text-brand-gold">{star_svg * 5}</div>'

def create_card(t):
    return f'''
<div class="w-80 md:w-96 bg-white rounded-2xl shadow-sm border border-gray-100 p-6 flex flex-col gap-4 flex-shrink-0">
    {stars}
    <p class="text-gray-600 text-sm italic leading-relaxed flex-grow">"{t['text']}"</p>
    <div class="pt-4 border-t border-gray-100 flex items-center gap-3">
        <div class="w-10 h-10 rounded-full bg-brand-navy flex items-center justify-center text-brand-gold font-bold font-heading">{get_initials(t['name'])}</div>
        <div>
            <h4 class="font-bold text-brand-navy text-sm">{t['name']}</h4>
            <span class="text-xs text-gray-500">Happy Client</span>
        </div>
    </div>
</div>'''

row1 = [testimonials[i] for i in [0,2,4,6,8,10]]
row2 = [testimonials[i] for i in [1,3,5,7,9,11]]

row1Cards = ''.join([create_card(t) for t in row1])
row2Cards = ''.join([create_card(t) for t in row2])

html = f'''
    <!-- Client Testimonials Section -->
    <section class="py-24 bg-brand-gray overflow-hidden">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mb-16 text-center reveal">
            <span class="inline-block bg-brand-gold/10 text-brand-gold text-xs font-bold uppercase tracking-widest px-4 py-1.5 rounded-full mb-4">Client Success Stories</span>
            <h2 class="font-heading text-4xl md:text-5xl font-bold text-brand-navy mb-4">What Our Clients Say</h2>
            <p class="text-gray-600 max-w-2xl mx-auto text-lg">Read about the experiences of our valued clients and how we've helped them secure prime real estate and commercial properties.</p>
        </div>

        <div class="relative w-full flex flex-col gap-6">
            <div class="absolute inset-y-0 left-0 w-16 md:w-32 bg-gradient-to-r from-brand-gray to-transparent z-10"></div>
            <div class="absolute inset-y-0 right-0 w-16 md:w-32 bg-gradient-to-l from-brand-gray to-transparent z-10"></div>

            <!-- Row 1 (Scroll Left) -->
            <div class="w-[300%] sm:w-[200%] lg:w-[150%] flex group">
                <div class="flex gap-6 animate-scroll-left group-hover:[animation-play-state:paused] w-1/2 justify-around px-3">
                    {row1Cards}
                </div>
                <div class="flex gap-6 animate-scroll-left group-hover:[animation-play-state:paused] w-1/2 justify-around px-3">
                    {row1Cards}
                </div>
            </div>

            <!-- Row 2 (Scroll Right) -->
            <div class="w-[300%] sm:w-[200%] lg:w-[150%] flex group">
                <div class="flex gap-6 animate-scroll-right group-hover:[animation-play-state:paused] w-1/2 justify-around px-3">
                    {row2Cards}
                </div>
                <div class="flex gap-6 animate-scroll-right group-hover:[animation-play-state:paused] w-1/2 justify-around px-3">
                    {row2Cards}
                </div>
            </div>
        </div>
    </section>
'''

with open('testimonials.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Saved to testimonials.html')
