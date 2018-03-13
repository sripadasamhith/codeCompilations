//
//  SecondViewController.swift
//  to do list
//
//  Created by Samhith Sripada on 2018-01-03.
//  Copyright © 2018 HackedApple. All rights reserved.
//

import UIKit

class SecondViewController: UIViewController, UITextFieldDelegate {

    
    @IBOutlet var textField: UITextField!
    
    
    @IBAction func addItemButton(_ sender: Any) {
        
        let itemObjects = UserDefaults.standard.object(forKey: "value")
        
        var items: [String]
        
        if var tempItems = itemObjects as? [String] {
            
            items = tempItems
            
            items.append(textField.text!)
            
        } else {
            
            items = [textField.text!]
            
        }
        
        UserDefaults.standard.set(items, forKey: "value")
        textField.text = ""
        
    }
    
    
    override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
        
        self.view.endEditing(true)
        
    }
    
    func textFieldShouldReturn(_ textField: UITextField) -> Bool {
        
        textField.resignFirstResponder()
        
        return true
        
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

