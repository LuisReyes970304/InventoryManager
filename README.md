<style>
    fieldset {
        border-radius: 10px;
        border: 1px solid rgb(10, 240, 100);
        color: rgb(108, 209, 78);
        background-color: black;
    }

    span {
        color: rgb(20, 200, 150);
        font-size: 18px;
        font-weight: 1000;
    }
</style>

<h1>InventoryManager</h1>

<p>This is a simple app that works in Console and help you out creating a product Inventory</p>

- Lest say that you have a business and you are buying some couple of products for your stock

- **InventoryManager** help you out crating a list of all the products name, quantity, price and even more, a total spent taking into account all the different classes of products.

<h2>How it works?</h2>
<p>InventoryManager is splited in four python files every one of them with an important function in the console application: </p>

<fieldset>

<legend> <h2>Files Function</h2> </legend>

- <h3>messages.py</h3> <p>This is the simples one, it take care of the styled message printed across the app, like the welcome message, the error messages and so on!<p>

- <h3>validation.py</h3> <p>This file takes care of the validation error and imports the sytled error messages from messages.py to look comfortable to the </p>

- <h3>inventory.py</h3> <p>This is the principal file in the app because it has the two main classes that make the application works, the <span>Product</span> and the <span>InventoryManager</span> classes</p>

- <h3>main.py</h3> <p>The main.py file is the place in which we put all the functions together in a loop and in this way the system runs until the client decide to stop it an get the final receipt with the inventory</p>

</fieldset>

