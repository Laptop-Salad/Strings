# Stiallan
An interpreted toy language that is written in Python and is dynamically typed.

[Installation](docs/Installation.md)

## Syntax
The syntax is similar to Scheme but has its differences.

All code should be enclosed in brackets.

### Math
```
(+ 5 5)
```

#### Types Of Operations
```
(+ 10 5)
(- 10 5)
(* 10 5)
(/ 10 5)
(% 10 5)
```

#### Nested Calculations
```
(+ 5 (- 10 3))
```

### Variables

```
(declare x as 5)
(declare x as 6)
```
Set x as 5, then 6.

#### Using Variables In Calculations
```
(declare x as 5)
(+ x x)
```
Returns 10.

## Roadmap
- [x]  Basic math operations
- [x]  Nested math operations
- [x]  Variables
- [ ]  Strings
- [ ]  Conditionals and booleans
- [ ]  Loops
- [ ]  Functions
- [ ]  Accept Files
