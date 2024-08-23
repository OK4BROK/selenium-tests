import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

def checkout():
        # checkout
        checkout_button = wait.until(EC.element_to_be_clickable((By.ID, 'top-cart-btn-checkout')))
        checkout_button.click()
        # fill shipping details
        email_input = wait.until(EC.visibility_of_element_located((By.ID, 'customer-email')))
        email_input.click()
        email = "razgus.deividas@gmail.com"
        email_input.send_keys(email)
        # name
        name_input = wait.until(EC.visibility_of_element_located((By.ID, 'AGLQC45')))
        name = "Deividas Razgus"
        name_input.send_keys(name)
        l_name_input = wait.until(EC.visibility_of_element_located((By.ID, 'CX7675V')))
        l_name_input.click()
        l_name = "Razgus"
        l_name_input.send_keys(l_name)
        # address
        address_input = wait.until(EC.visibility_of_element_located((By.ID, 'L743SYK'))) 
        address_input.click()
        address = "Didlaukio 59"
        address_input.send_keys(address)
        # city
        city_input = wait.until(EC.visibility_of_element_located((By.ID, 'F9FX1UJ'))) 
        city_input.click()
        city = "Vilnius"
        city_input.send_keys(city)
        # province
        dropdown = wait.until(EC.visibility_of_element_located((By.ID, 'FQ9L4JE')))
        select = Select(dropdown)
        select.select_by_value('43')
        # zip code
        postal_code_input = wait.until(EC.visibility_of_element_located((By.ID, 'A0WSG8X'))) 
        postal_code_input.click()
        postal_code = "89165"
        postal_code_input.send_keys(postal_code)
        #country
        country_dropdown = wait.until(EC.visibility_of_element_located((By.ID, 'HFYQSEY')))
        select = Select(country_dropdown)
        select.select_by_visible_text('Lithuania')
        # phone number
        phone_number_input = wait.until(EC.visibility_of_element_located((By.ID, 'O9MGWC4')))
        phone_number_input.click()
        ph_number = "+37061215598"
        phone_number_input.send_keys(ph_number)
        #shipping 
        shipping_available = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='radio'][value='flatrate_flatrate']")))
        shipping_available.click()
        #place the order 
        place_order_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.action.primary.checkout[type='submit']")))
        place_order_button.click()

def test_magento_sc1():
    driver = webdriver.Chrome() 
    driver.get("https://magento.softwaretestingboard.com/")
    
    def count_products():
        # Wait 10 seconds to ensure everything has loaded
        wait = WebDriverWait(driver, 10)
    
        # Navigate to the product listing page making sure contents have loaded
        driver.find_element(By.LINK_TEXT, "Men").click()
        wait.until(EC.element_to_be_clickable(By.LINK_TEXT, "Tops")).click()
        wait.until(EC.element_to_be_clickable(By.LINK_TEXT, "Hoodies & Sweatshirts")).click()
        
        # Wait for the products to be visible
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "ol.products.list.items.product-items")))
        
        # get the expected ammount of products
        expected_count = driver.find_element(By.CLASS_NAME,"limiter") 
        # count the actual number of products
        actual_count = len(driver.find_elements(By.CSS_SELECTOR, "li.item.product.product-item")) 
        #compare expected and actual ammount of products
        assert expected_count == actual_count, f"Expected {expected_count} products, but found {actual_count}"
    count_products()
    # select frankie sweatshirt
    driver.find_element(By.LINK_TEXT, "Men").click()
    driver.find_element(By.LINK_TEXT, "Tops").click()
    driver.find_element(By.LINK_TEXT, "Hoodies & Sweatshirts").click()
    driver.find_element(By.CSS_SELECTOR,"img[alt='Frankie Sweatshirt']").click()
    wait = WebDriverWait(driver, 10)
    # select the size xs
    size_m = driver.find_element(By.ID, "option-label-size-143-item-166")
    size_m.click()
    # select color green 
    color_green = driver.find_element(By.ID,"option-label-color-93-item-53" ).click
    # choose quantity
    quantity_input = driver.find_element((By.ID, 'qty'))
    quantity_input.clear()
    # choose quantity of 2
    quantity_input = wait.until(EC.element_to_be_clickable((By.ID, 'qty')))
    quantity = 2
    quantity_input.send_keys(str(quantity))
    # add to cart
    add_to_cart = wait.until(EC.element_to_be_clickable((By.ID, 'product-addtocart-button')))
    add_to_cart.click()
    # open cart 
    cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.action.showcart')))
    cart_button.click()
    # check if cart qty updated
    cart_quantity_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span.counter-number')))
    cart_quantity = cart_quantity_element.text.strip()
    assert cart_quantity == quantity, f"Cart icon quantity {cart_quantity}, chosen quantity {quantity}"
    # check if product in cart is correct
    product_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[data-bind*='product_name']")))
    cart_product_name = product_link.text
    chosen_product_name = "Frankie Sweatshirt"
    assert cart_product_name == chosen_product_name, f" Chosen product is {expected_product_name} the product in cart is {product_name}"
    #checkout
    checkout()
    
def test_magento_sc2():
    driver = webdriver.Chrome() 
    driver.get("https://magento.softwaretestingboard.com/")
    # Wait 10 seconds to ensure everything has loaded
    wait = WebDriverWait(driver, 10)
    # choose womens pants
    driver.find_element(By.LINK_TEXT, "Women").click()
    driver.find_element(By.LINK_TEXT, "Bottoms").click()
    driver.find_element(By.LINK_TEXT, "Pants").click()
    # sort by price
    sorter_dropdown = wait.until(EC.visibility_of_element_located((By.ID, 'sorter')))
    select = Select(sorter_dropdown)
    select.select_by_visible_text('Price')
    #choose the cheapest product
    products = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.product-list-items')))
    cheapest_product = products[0]
    cheapest_product_link = cheapest_product.find_element(By.CSS_SELECTOR, '[data-product-id="1819"]')
    cheapest_product_link.click()
    # select the size 
    size_option = wait.until(EC.element_to_be_clickable((By.ID, "option-label-size-143-item-171")))
    size_option.click()m,
    #select color
    color_option = wait.until(EC.element_to_be_clickable((By.ID, "option-label-color-93-item-50")))
    color_option.click()

    # add to cart
    add_to_cart = wait.until(EC.element_to_be_clickable((By.ID, 'product-addtocart-button')))
    add_to_cart.click()
    #add  1 more product
    emma_leggings = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.product-item-link[title='Emma Leggings']")))
    emma_leggins.click()
    # select the size 
    size_option = wait.until(EC.element_to_be_clickable((By.ID, "option-label-size-143-item-171")))
    size_option.click()
    #select color
    color_option = wait.until(EC.element_to_be_clickable((By.ID, "option-label-color-93-item-50")))
    color_option.click()
    #add to cart 
    add_to_cart = wait.until(EC.element_to_be_clickable((By.ID, 'product-addtocart-button')))
    add_to_cart.click()
    #add  1 more product
    ida_workout = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.product-item-link[title='Ida Workout Parachute Pant']")))
    ida_workout.click()
    # select the size 
    size_option = wait.until(EC.element_to_be_clickable((By.ID, "option-label-size-143-item-171")))
    size_option.click()
    #select color
    color_option = wait.until(EC.element_to_be_clickable((By.ID, "option-label-color-93-item-50")))
    color_option.click()
    #add to cart 
    add_to_cart = wait.until(EC.element_to_be_clickable((By.ID, 'product-addtocart-button')))
    add_to_cart.click()
    # open cart 
    cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.action.showcart')))
    cart_button.click()
    #remove product
    remove_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.action.delete[data-cart-item='268437']")))
    remove_button.click()
    ok_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.action-primary.action-accept[data-role='action']")))
    ok.button.click()
    #add product from recommended
    cora_recc = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "img.product-image-photo[alt='Cora Parachute Pant']")))
    cora_recc.click()
    #checkout
    checkout()


    # Close the browser
    driver.quit()
