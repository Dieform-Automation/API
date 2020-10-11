# API Guide
![Deploy](https://github.com/Dieform-Automation/API/workflows/Deploy/badge.svg)


# Live API Link + Swagger UI
https://shielded-lake-43806.herokuapp.com/

## Customer
| Method | Action | Endpoint  | Arguments | Body | Complete |
|---|---|---|---|---|:---:|
|GET | Get all customers | /customer/ | - | - | <ul><li>- [x] </li></ul> |
|GET | Get customer by id |  /customer/id | - | - | <ul><li>- [x] </li></ul>  |
|POST| Add customer | /customer/ | -  | name, point_of_contact, email, street, city, province, country, postal code, phone | <ul><li>- [x] </li></ul>  |
|PUT| Update customer | /customer/id | - | name, point_of_contact, email, street, city, province, country, postal code, phone | <ul><li>- [x] </li></ul>  |

## Part
| Method | Action | Endpoint  | Arguments | Body | Complete |
|---|---|---|---|---|:---:|
|GET | Get all parts | /part/ | - | - | <ul><li>- [x] </li></ul> |
|GET | Get part by id |  /part/id | - | - | <ul><li>- [x] </li></ul>  |
|GET | Get all parts by customer_id |  /part? | customer_id | - | <ul><li>- [x] </li></ul>  |
|POST| Add part | /part/ | - | number, name, purchase_order_id, customer_id | <ul><li>- [x] </li></ul>  |
|PUT| Update part | /part/id | - | name | <ul><li>- [x] </li></ul>  |

## Order
| Method | Action | Endpoint  | Arguments | Body | Complete |
|---|---|---|---|---|:---:|
|GET | Get all orders | /order/ | - | - | <ul><li>- [x] </li></ul> |
|GET | Get order by id |  /order/id | - | - | <ul><li>- [x] </li></ul>  |
|GET | Get all orders by customer_id |  /order? | customer_id | - | <ul><li>- [x] </li></ul>  |
|POST| Add order | /order/ | - | customer_id, order_number, list of part_ids (mapped to quantity) | <ul><li>- [x] </li></ul>  |
|PUT| Update order | /order/id | - | list of part_ids (mapped to quantity) | <ul><li>- [x] </li></ul>  |

## Recieving
| Method | Action | Endpoint  | Arguments | Body | Complete |
|---|---|---|---|---|:---:|
|GET | Get all receivables | /recieving/ | - | - | <ul><li>- [x] </li></ul> |
|GET | Get receivable by id |  /recieving/id | - | - | <ul><li>- [x] </li></ul>  |
|GET | Get all receivables by customer_id |  /recieving? | customer_id | - | <ul><li>- [x] </li></ul>  |
|POST| Add receivable | /recieving/ | - | customer_id, part_id, customer_packing_slip, part_quantity, date* | <ul><li>- [x] </li></ul>  |
|PUT| Update receivable | /recieving/id | - | customer_id, part_id, customer_packing_slip, part_quantity, date | <ul><li>- [x] </li></ul>  |
