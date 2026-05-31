class Supplier:
    supplier_count = 0
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact
        Supplier.supplier_count += 1
    def display_supplier(self):
        print("Supplier Name : " + self.name)
        print("Contact       : " + self.contact)
    @staticmethod
    def get_supplier_count():
        return Supplier.supplier_count
class Product:
    product_count = 0
    class Specification:
        def __init__(self, weight, color, material):
            self.weight = weight
            self.color = color
            self.material = material
        def display_spec(self):
            print("  Specifications:")
            print("    Weight   : " + self.weight)
            print("    Color    : " + self.color)
            print("    Material : " + self.material)
    def __init__(self, pid, name, price, supplier, weight, color, material):
        self.pid = pid
        self.name = name
        self.price = price
        self.supplier = supplier
        self.spec = Product.Specification(weight, color, material)
        Product.product_count += 1
    def display_product(self):
        print("\nProduct ID : " + str(self.pid))
        print("Name       : " + self.name)
        print("Price      : " + str(self.price))
        self.supplier.display_supplier()
        self.spec.display_spec()
    @staticmethod
    def get_product_count():
        return Product.product_count
products = []
n = int(input("Enter number of products: "))
for i in range(n):
    print("\nEnter details for product " + str(i+1))
    sname = input("Supplier name: ")
    scontact = input("Supplier contact: ")
    supplier = Supplier(sname, scontact)
    pid = input("Product ID: ")
    pname = input("Product name: ")
    price = float(input("Price: "))
    weight = input("Weight: ")
    color = input("Color: ")
    material = input("Material: ")
    product = Product(pid, pname, price, supplier, weight, color, material)
    products.append(product)
print("\n---- Product Information ----")
for p in products:
    p.display_product()
print("\nTotal Products: " + str(Product.get_product_count()))
print("Total Suppliers: " + str(Supplier.get_supplier_count()))