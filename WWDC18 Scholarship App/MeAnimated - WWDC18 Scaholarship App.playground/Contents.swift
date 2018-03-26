//: Playground - noun: a place where people can play

import UIKit
import PlaygroundSupport
import SpriteKit

// var str = "Hello, playground"

class myView: UIView {

    /*

    extension UIColor {
     
        static let newRed = UIColor.init(red: 238.0, green: 56.0, blue: 56.0, alpha: 1.0)

        static let newGreen = UIColor.init(red: 29.0, green: 209.0, blue: 85.0, alpha: 1.0)

        static let newBlue = UIColor.init(red: 6.0, green: 105.0, blue: 214.0, alpha: 1.0)
     
    }



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
     
    // Animated Apple Logo onto Screen
     
    */


    override func draw(_ rect: CGRect) {
        
//        let line = UIBezierPath()
//        line.move(to: CGPoint(x: 200, y: 350))
//        line.addLine(to: CGPoint(x: 200, y: 100))
//        line.addLine(to: CGPoint(x: 200, y: 500))
//        line.lineWidth = 5.0
//        UIColor.gray.setStroke()
//        line.stroke()
//        line.close()
        
        // Straight line
        
//        let quadCurve = UIBezierPath()
//
//        let start = CGPoint(x: 75, y: 200)
//        let end = CGPoint(x: 290, y: 345)
//        let control = CGPoint(x: 200, y: 75)
//
//        quadCurve.move(to: start)
//        quadCurve.addQuadCurve(to: end, controlPoint: control)
//        quadCurve.lineWidth = 5.0
//        UIColor.blue.setStroke()
//        quadCurve.stroke()
//
//        // Curved line
        
    let cubicCurve = UIBezierPath()

    let cubicStart = CGPoint(x: 125, y: 100)
    let cubicEnd = CGPoint(x: 600, y: 465)
    let cubicControl1 = CGPoint(x: 10, y: 100)
    let cubicControl2 = CGPoint(x: 125, y: 300)

    cubicCurve.move(to: cubicStart)
    cubicCurve.addCurve(to: cubicEnd, controlPoint1: cubicControl1, controlPoint2: cubicControl2)
    cubicCurve.lineWidth = 5.0
    UIColor.orange.setStroke()
    cubicCurve.stroke()

    // Cubic Curve
        

    }
    
}

let view = myView(frame: CGRect(x: 0.0, y: 0.0, width: 925, height: 925))
view.backgroundColor = UIColor.white
PlaygroundPage.current.liveView = view















