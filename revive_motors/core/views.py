from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Car, Transaction
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

'''
INSERT INTO auth_user (username, first_name, last_name, email, password, is_staff, is_active, date_joined) 
VALUES ('email@example.com', 'First', 'Last', 'email@example.com', 'hashed_password', 0, 1, NOW());
'''

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username = email, first_name=first_name, last_name=last_name, email=email, password=password)
        user.save()
        messages.success(request, 'Account created successfully!')
        return redirect('home')
    return render(request, 'register.html')


'''
SELECT * 
FROM auth_user 
WHERE username = 'username' AND password = 'hashed_password';
'''

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid email or password.')
    return render(request, 'login.html')



def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout successful!')
    return redirect('home')


'''
SELECT * 
FROM table_name;
'''

def shop(request):
    cars = Car.objects.all()
    return render(request, 'shop.html', {'cars': cars})


'''
SELECT * 
FROM table_name 
WHERE id = car_id;
'''

def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    brand = car.brand
    model = car.model
    year = car.year
    price = car.price
    condition = car.condition
    description = car.description
    photo = car.photo
    current_owner = car.current_owner
    mileage = car.mileage
    transmission = car.transmission

    car = {
        'brand': brand,
        'model': model,
        'year': year,
        'price': price,
        'condition': condition,
        'description': description,
        'photo': photo,
        'current_owner': current_owner,
        'mileage': mileage,
        'transmission': transmission
    }
    return render(request, 'car_detail.html', {'car': car})



'''
  SELECT * 
  FROM app_car 
  WHERE brand LIKE '%brand%' 
    AND model LIKE '%model%' 
    AND (year = year_value OR year_value IS NULL) 
    AND (price BETWEEN min_price AND max_price OR (min_price IS NULL AND max_price IS NULL)) 
 ORDER BY price ASC; -- or DESC based on sort_price
'''

def filtered_shop(request):
    cars = Car.objects.all()
    
    if request.method == 'POST':
        filters = {
            'brand__icontains': request.POST.get('brand'),
            'model__icontains': request.POST.get('model'),
            'year': request.POST.get('year'),
            'price__gte': request.POST.get('price_min'),
            'price__lte': request.POST.get('price_max'),
        }
        
        sort_price = request.POST.get('sort_price')
        
        if sort_price == 'asc':
            cars = cars.order_by('price')
        elif sort_price == 'desc':
            cars = cars.order_by('-price')

        filters = {k: v for k, v in filters.items() if v}
        
        cars = cars.filter(**filters)
    
        return render(request, 'filtered_shop.html', {'cars': cars})
    redirect('shop')




'''
-- Insert transaction
INSERT INTO app_transaction (buyer_id, seller_id, car_id, transaction_date, price) 
VALUES (buyer_id, seller_id, car_id, NOW(), car_price);

-- Update car ownership
UPDATE app_car 
SET current_owner_id = buyer_id 
WHERE id = car_id;
'''

@login_required
def buy_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if car.current_owner == request.user:
        return render(request, 'buy_car.html', {'error': 'You cannot buy your own car!'})
    else:
        transaction = Transaction.objects.create(
            buyer=request.user,
            seller=car.current_owner,
            car=car,
            price=car.price,
        )
        transaction.save()

        car.current_owner = request.user
        car.save()

        show_transaction = {
            'buyer': transaction.buyer.username,
            'seller': transaction.seller.username,
            'car': f"{car.brand} {car.model} ({car.year})",
            'price': car.price,
        }

        return render(request, 'buy_car.html', {'transaction': show_transaction})



'''
INSERT INTO app_car (brand, model, year, price, condition, mileage, transmission, description, photo, current_owner_id, available_for_sale) 
VALUES ('brand', 'model', year_value, price_value, 'condition', mileage_value, 'transmission', 'description', 'photo_url', user_id, on_sale_flag);
'''

@login_required
def sell_car(request):
    if request.method == 'POST':
        brand = request.POST['brand']
        model = request.POST['model']
        year = request.POST['year']
        price = request.POST['price']
        condition = request.POST['condition']
        mileage = request.POST['mileage']
        transmission = request.POST['transmission']
        description = request.POST['description']
        photo = request.POST['photo']
        on_sale = request.POST['on_sale']
        if on_sale == 'yes':
            on_sale = True
        else:
            on_sale = False
        car = Car.objects.create(
            brand=brand,
            model=model,
            year=year,
            price=price,
            condition=condition,
            mileage=mileage,
            transmission=transmission,
            description=description,
            photo=photo,
            current_owner=request.user,
            available_for_sale=on_sale
        )
        car.save()
        messages.success(request, 'Car listed for sale successfully!')
        return redirect('shop')
    return render(request, 'sell_car.html')



'''
# UPDATE app_car 
SET brand = 'brand', 
    model = 'model', 
    year = year_value, 
    price = price_value, 
    condition = 'condition', 
    mileage = mileage_value, 
    transmission = 'transmission', 
    description = 'description', 
    photo = 'photo_url', 
    available_for_sale = on_sale_flag 
WHERE id = car_id AND current_owner_id = user_id;
'''

@login_required
def update_car(request, car_id):
    car = get_object_or_404(Car, id=car_id, current_owner=request.user)
    if request.method == 'POST':
        car.brand = request.POST['brand']
        car.model = request.POST['model']
        car.year = request.POST['year']
        car.price = request.POST['price']
        car.condition = request.POST['condition']
        car.mileage = request.POST['mileage']
        car.transmission = request.POST['transmission']
        car.description = request.POST['description']
        car.photo = request.POST['photo']
        on_sale = request.POST['on_sale']
        car.available_for_sale = True if on_sale == 'yes' else False
        car.save()
        messages.success(request, 'Car details updated successfully!')
        return redirect('shop')
    return render(request, 'update_car.html', {'car': car})



'''
DELETE 
FROM app_car 
WHERE id = car_id AND current_owner_id = user_id;
'''

@login_required
def delete_car(request, car_id):
    car = get_object_or_404(Car, id=car_id, current_owner=request.user)
    if request.method == 'POST':
        car.delete()
        messages.success(request, 'Car removed successfully!')
        return redirect('shop')
    return redirect('shop')


'''
--- BUYER TRANSACTION ---
SELECT * 
FROM app_transaction 
WHERE buyer_id = user_id;

--- SELLER TRANSACTION ---
SELECT * 
FROM app_transaction 
WHERE seller_id = user_id;
'''

@login_required
def transaction_history(request):
    transaction_obj = Transaction.objects.all()
    buying_transactions = transaction_obj.filter(buyer=request.user)
    selling_transactions = transaction_obj.filter(seller=request.user)
    return render(request, 'transaction_history.html', {
        'buying_transactions': buying_transactions,
        'selling_transactions': selling_transactions
    })




def about_us(request):
    return render(request, 'about_us.html')




@login_required
def contact_us(request):
    if request.method == 'POST':
        return HttpResponse('Thank you for contacting us! We will get back to you soon.')
    return render(request, 'contact_admin.html')