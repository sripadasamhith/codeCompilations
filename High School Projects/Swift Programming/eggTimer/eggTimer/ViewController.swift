//
//  ViewController.swift
//  eggTimer
//
//  Created by Samhith Sripada on 2017-12-13.
//  Copyright © 2017 HackedApple. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    
    var seconds = 210
    var timer = Timer()
    var isRunning = true
    var resumeTapped = false
    
    
    @objc func runTimer() {
        
        timer = Timer.scheduledTimer(timeInterval: 1, target: self, selector: #selector(ViewController.updateSeconds), userInfo: nil, repeats: true)
        
    }
    
    
    
    @IBAction func pause(_ sender: Any) {
        
        if self.resumeTapped == false {
            timer.invalidate()
            self.resumeTapped = true
            secondsLabel.text = "\(seconds) sec"
            isRunning = false
        }
        
    }
    
    
    @IBAction func play(_ sender: Any) {
        
        if isRunning == false {
        
            runTimer()
            secondsLabel.text = "\(seconds) sec"
        
        } else {
            
            timer.invalidate()
            
            
        }
    }
    
    @IBOutlet weak var secondsLabel: UILabel!
    
    
    @objc func updateSeconds() {
        
        seconds -= 1
        secondsLabel.text = "\(seconds) sec"
        
        
    }
    
    
    @IBAction func lessTen(_ sender: Any) {
        
        seconds -= 10
        secondsLabel.text = "\(seconds) sec"
        
    }
    
    
    @IBAction func reset(_ sender: Any) {
        
        seconds += 210 - seconds
        secondsLabel.text = "\(seconds) sec"
        
    }
    
    
    @IBAction func addTen(_ sender: Any) {
        
        seconds += 10
        secondsLabel.text = "\(seconds) sec"
        
    }
    
    
    
    
    
    
    
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        
        
    }
    
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}

