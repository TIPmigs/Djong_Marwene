from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=GEMINI_API_KEY)

# Function to generate tags
def generate_tags(name, description):
    try:
        prompt = f"Generate 5 relevant, comma-separated product tags for this item:\nName: {name}\nDescription: {description}\n\nTags:"
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        tag_string = response.text.strip()
        tags = [tag.strip() for tag in tag_string.split(',') if tag.strip()]
        return tags
    except Exception as e:
        print("Gemini error:", e)
        return []

# Show product list
def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

# Add product and auto-tag
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)

            tags = generate_tags(product.name, product.description)
            print(f"Generated Tags: {tags}")  

            if tags:
                product.tags = ', '.join(tags)
            else:
                print("No tags generated")  
            product.save()
            print(f"Product saved with tags: {product.tags}") 

            return redirect('product_list')
    else:
        form = ProductForm()
    
    return render(request, 'store/add_product.html', {'form': form})
