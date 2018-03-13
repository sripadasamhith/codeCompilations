//
//  ViewController.swift
//  Storing Data Permanently
//
//  Created by Samhith Sripada on 2018-01-02.
//  Copyright © 2018 HackedApple. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    
    @IBOutlet var phoneNumber: UITextField!
    
    
    @IBAction func save(_ sender: Any) {
        
        UserDefaults.standard.set(phoneNumber.text, forKey: "phoneNumber")
        
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    
        let phoneNumberObject = UserDefaults.standard.object(forKey: "phoneNumber")
        
        if let number = phoneNumberObject as? String {
            
            phoneNumber.text = number
            
        }
        
        func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}


}
