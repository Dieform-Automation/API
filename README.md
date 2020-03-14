# API Guide
![Push Container to Heroku](https://github.com/Dieform-Automation/API/workflows/Push%20Container%20to%20Heroku/badge.svg)

# Live API Link + Swagger UI
https://shielded-lake-43806.herokuapp.com/

## Customer

- [x] GET all customers
- [ ] GET customer by id
- [ ] POST add customer(name, point_of_contact, email, street, city, province, country, postal code, phone)
- [ ] POST update customer(name, point_of_contact, email, street, city, province, country, postal code, phone)


## Part

- [ ] GET all parts
- [ ] GET all parts by customer_id
- [ ] GET all parts by order_id
- [ ] GET part by id
- [ ] POST add new part(number, name, customer_id)
- [ ] POST update new part(name)

## Order

- [ ] GET all orders (return parts by order_id)
- [ ] GET all orders by customer_id
- [ ] POST add new order(customer_id, order_number, list of part_ids (mapped to quantity))
- [ ] POST add new part to order(order_id, part_id, quantity)
