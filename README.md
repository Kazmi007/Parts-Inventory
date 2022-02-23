# Tool-for-Construction-Logistics
A program that takes a parts-list (including all elements at different abstraction levels), for a single constructed component, as an input and implements a tree to calculate the total price, total required basic parts, and whether those required parts exist in the stock (represented as a stock-list).

The code is implemented in python 3.0 and each operation is implemented as a function.
Parts-list is a list of lists where each element in the primary list is either a constructed component or a base component. For contructed components, the list element must be a list with its first element being the name of the component (as string), followed by 2-tuples of its constituent components as '(amount_required,component_name)'. The base components are represented as a list like '[part_name, price]'.
Stock-list is implemented as a list of 2-tuples where each tuple is '(amount,part_name)'.

Hope its helpful :)
