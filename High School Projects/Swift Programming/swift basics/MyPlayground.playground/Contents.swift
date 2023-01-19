import UIKit

var str = "Hello, playground"

/**********
 
Swift basics playground

**********/


//// Variables
//
//let NAME = "Samhith"
//var greeting = "Welcome, " + NAME + "!"
//
//print(greeting)
//print("My name is \(NAME)")
//
//// Floats and doubles are faster and efficient --- decimal is most accurate
//
//// Arrays
//
//var famNames = ["Rajesh", "Vani", "Samhith", "Sriya"]
//
//famNames.append("Rajeswari")
//
//print(famNames)
//
//famNames.remove(at: famNames.count - 1)
//
//print(famNames)
//
//// Dictionaries
//
//var pplDictionary = ["Rajesh" : "Father", "Vani" : "Mother", "Samhith" : "Son", "Sriya" : "Daughter"]
//
//print(pplDictionary["Rajesh"]!) // '!' used when you know the value exists
//
//pplDictionary["Rajeswari"] = "Grandmother"
//pplDictionary["BLANK"] = "REMOVE"
//pplDictionary.removeValue(forKey: "BLANK")
//
//print(pplDictionary.count)
//
//var appleProducts = [String : Int]() // When defining empty dictionaries, always include () at the end of declaration
//
//appleProducts["iPhone"] = 5
//appleProducts["Mac Mini"] = 1
//
//print(appleProducts)
//
//// Conditionals
//
//var ageOfUser = 18
//
//if ageOfUser >= 18 {
//
//    print("You can play!")
//
//} else {
//
//    print("Grow older!")
//
//}
//
//var nameOfUser = "Sam"
//
//if nameOfUser != "Sam" {
//
//    print("Wrong person!")
//
//} else {
//
//    print("YAYAYAYAYAYAYAY!!!!")
//
//} // A continuation would be followed using else if... same operands as other languages such as &&, ||
//
//let randomNum = arc4random_uniform(100)
//
//print(randomNum)
//
//// While Loops
//
//var i = 0
//
//while i < 10 {
//
//    print(i)
//    i += 1 // += is the swift incremental
//
//}
//
//var counter = 1
//
//while counter <= 20 {
//
//    print(7 * counter)
//    counter += 1
//
//}
//
//var i = 0
//
//var array = [5,6,32,543,52,65]
//
//while i < array.count {
//
//    array[i] += 1
//    i += 1
//
//}
//
//print(array)
//
// For Loops
//
//var array = [2,5,32,543,6]
//
//for number in array {
//
//    print(number)
//
//}
//
//var names = ["sam","sri","raj","van"]
//
//for people in names {
//
//    print("Hello \(people)!")
//
//}
//
//var numbers = [2,5,32,543,6]
//
//for (index, value) in numbers.enumerated() {
//
//    numbers[index] += 1
//
//}
//
//print(numbers)
//
//var halves = [8.0,7.0,19.0,28.0] // Can also be declared as: var halves = [Double](); halves = [8,7,19,28]
//
//for (index, value) in halves.enumerated() {
//
//    halves[index] = value / 2 // value is a temporary variable
//
//}
//
//print(halves)
//
// Classes and Objects
//
//class Car {
//
//    // Classes start with a capital letter
//    // We can set various attributes pertaining to Cars class
//
//    var isMoving = false
//    var make = "Lexus"
//    var model = "RX350"
//    var year = "2012"
//
//    func move() {
//
//        isMoving = true
//
//    }
//
//    func isTurnedOn() -> Bool {
//
//        if isMoving {
//
//            return true
//
//        } else {
//
//            return false
//
//        }
//
//    }
//
//}
//
//var car = Car() // setting an object from cars class
//
//print(car.isMoving)
//
//car.make = "Tesla"
//
//print(car.make)
//
//car.move()
//
//print(car.isMoving)
//
//print(car.isTurnedOn())
//
//car.isMoving = false
//
//print(car.isTurnedOn())
//
// Optionals

// Its possible to create empty variables
// Using these variables throws errrors
// Optionals allow ppl to use variables without knowing if there is an absolute value
//
//var number: Int?
//print(number)
//
//let userText = "three"
//
//let userInt = Int(userText)
//
//if let catAge = userInt {
//
//    print(catAge * 7)
//
//}
//
//// Code above prevent forced unwrapping optional variables
//// Prevents let catAge = userInt!
//
//
// Extensions
//
// Extensions allow you to expand the functionality of an existing class(es)
//
//extension String {
//
//    func reverse() -> String {
//
//        var charArray = [Character]()
//
//        for character in self.characters {
//
//            charArray.insert(character, at: 0)
//
//        }
//
//        return String(charArray)
//
//    }
//
//}
//
//var name = "samhith"
//
//name.reverse()
//
// 
