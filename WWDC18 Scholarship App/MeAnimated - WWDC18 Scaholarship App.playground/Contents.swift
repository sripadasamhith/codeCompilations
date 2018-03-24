//: Playground - noun: a place where people can play

import UIKit
import PlaygroundSupport
import SpriteKit

// var str = "Hello, playground"

let view = UIView(frame: CGRect(x: 0.0, y: 0.0, width: 500, height: 300))

let linePath = UIBezierPath()
let arcCenter = CGPoint()

linePath.addArc(withCenter: arcCenter, radius: 50, startAngle: 0, endAngle: 360, clockwise: true)

PlaygroundPage.current.liveView = view
