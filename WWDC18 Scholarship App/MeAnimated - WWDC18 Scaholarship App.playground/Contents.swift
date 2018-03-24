//: Playground - noun: a place where people can play

import UIKit
import PlaygroundSupport
import SpriteKit

// var str = "Hello, playground"



let view = UIView(frame: CGRect(x: 0.0, y: 0.0, width: 400, height: 700))
view.backgroundColor = UIColor.white

extension UIColor {
    
    static let newRed = UIColor.init(red: 238.0, green: 56.0, blue: 56.0, alpha: 1.0)

    static let newGreen = UIColor.init(red: 29.0, green: 209.0, blue: 85.0, alpha: 1.0)

    static let newBlue = UIColor.init(red: 6.0, green: 105.0, blue: 214.0, alpha: 1.0)
    
}


/*
let linePath = UIBezierPath()
let arcCenter = CGPoint()

linePath.addArc(withCenter: arcCenter, radius: 50, startAngle: 0, endAngle: 360, clockwise: true)

*/

let circle = UIView(frame: CGRect(x: 137.5, y: 400, width: 150, height: 150))

circle.center = view.center

circle.backgroundColor = UIColor.red
circle.layer.borderColor = UIColor.red.cgColor
circle.layer.cornerRadius = 30.0
circle.layer.borderWidth = 3.5

view.addSubview(circle)
// circle

let appleImage = UIImageView(frame: CGRect(x: 137.5, y: 10, width: 125, height: 125))
appleImage.image = UIImage(named: "appleLogoPNG.png")
view.addSubview(appleImage)
// apple logo

let rotate = CGAffineTransform(rotationAngle: 360.0)
// rotate

let scale = CGAffineTransform(scaleX: 2, y: 2)

UIView.animate(withDuration: 1.5, animations: {() -> Void in
    
    appleImage.center = view.center
    circle.transform = rotate.concatenating(scale)
    circle.layer.cornerRadius = 75.0
    circle.backgroundColor = UIColor.green
    circle.layer.borderColor = UIColor.white.cgColor
    
})

PlaygroundPage.current.liveView = view



