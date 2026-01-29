import os
import datetime
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

# server setup
FRONTEND_FOLDER = os.path.abspath("../frontend")
app = Flask(__name__, static_folder=FRONTEND_FOLDER, static_url_path='')
CORS(app)


# chatbot knowledge base
RESUME_DATA = {
    "grades": "Kristina has an outstanding GPA of 97.13. Her top grades are: Data Structures (100), Intro to CS (100), Computer Systems (98). you can see more details on her grades in the Education section of her portfolio.",
    
    "experience": "Kristina served as an IDF Course Commander (2020-2024). She led professional training for advanced tech systems and managed mission-critical tasks under pressure.",
    
    "skills": "Kristina specializes in Python, C++, C#, C, and Java Script. She is proficient in Data Structures, Algorithms, and uses tools like Git and Linux.",
    
    "projects": "Kristina is currently working on new projects, focusing on mastering AI and Computer Vision Python libraries to build a Virtual Mouse system.",
    
    "contact": "You can reach Kristina at 053-3341226 or via email at kristinasner200293@gmail.com.",
    
    "strengths": "Why hire Kristina? She combines a high GPA (97.13) with leadership experience from her IDF service. She is a fast learner, currently teaching herself new technologies. She is highly motivated to integrate into challenging positions and is committed to everything she takes upon herself",
    
    "goals": "Kristina is looking for her first student Developer or DevOps role where she can tackle complex challenges and grow within a strong engineering team.",
    
    "hobbies": "Beyond coding, Kristina enjoys solving logic puzzles and exploring new technologies.",
    
    "availability": "Kristina is available for immediate interviews and can start a student position",

    "default": "I am Kristina's AI Assistant. Ask me about her Grades, Experience, Skills, Projects, or why you should hire her!"
}

# rotes for serving frontend
@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

# --- API Endpoints ---

@app.route('/api/daily-challenge', methods=['GET'])
def get_daily_challenge():
    problems = [
        {
            "title": "Two Sum", 
            "difficulty": "Easy", 
            "description": "Given an array of integers, return indices of the two numbers such that they add up to a specific target.", 
            "link": "https://leetcode.com/problems/two-sum/"
        },
        {
            "title": "Valid Parentheses", 
            "difficulty": "Easy", 
            "description": "Check if the input string has valid brackets: '()', '{}', '[]'.", 
            "link": "https://leetcode.com/problems/valid-parentheses/"
        },
        {
            "title": "Longest Substring", 
            "difficulty": "Medium", 
            "description": "Find the length of the longest substring without repeating characters.", 
            "link": "https://leetcode.com/problems/longest-substring-without-repeating-characters/"
        },
        {
            "title": "Maximum Subarray", 
            "difficulty": "Medium", 
            "description": "Find the subarray with the largest sum and return its sum.", 
            "link": "https://leetcode.com/problems/maximum-subarray/"
        },
        {
            "title": "Climbing Stairs", 
            "difficulty": "Easy", 
            "description": "You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. How many ways?", 
            "link": "https://leetcode.com/problems/climbing-stairs/"
        },
       {
            "title": "Roman to Integer", 
            "difficulty": "Easy", 
            "description": "Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.",
            "link": "https://leetcode.com/problems/roman-to-integer/?envType=problem-list-v2&envId=hash-table"
        },
         {
            "title": "Group Anagrams", 
            "difficulty": "Medium", 
            "description": "Given an array of strings strs, group the anagrams together. You can return the answer in any order.",
            "link": "https://leetcode.com/problems/group-anagrams/description/?envType=problem-list-v2&envId=hash-table"
        },
         {
            "title": "Construct Binary Tree from Inorder and Postorder Traversal", 
            "difficulty": "Medium", 
            "description": "Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.",
            "link": "https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/?envType=problem-list-v2&envId=hash-table"
        },
            {
            "title": "Copy List with Random Pointer",
            "difficulty": "Medium", 
            "description": "A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null. Your task is to return a deep copy of the list.",
            "link": "https://leetcode.com/problems/copy-list-with-random-pointer/description/?envType=problem-list-v2&envId=hash-table"
        },
            {
            "title": "Fraction to Recurring Decimal",
            "difficulty": "Medium", 
            "description": "Given two integers representing the numerator and denominator of a fraction, return the fraction in string format. If the fractional part is repeating, enclose the repeating part in parentheses.",
            "link": "https://leetcode.com/problems/fraction-to-recurring-decimal/description/?envType=problem-list-v2&envId=hash-table"
        },
            {
            "title": "Jump Game II",
            "difficulty": "Medium", 
            "description": "You are given a 0-indexed array of integers nums of length n. You are initially positioned at index 0. Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at index i, you can jump to any index in the range [i + 1, i + nums[i]] inclusive. Your goal is to reach the last index of the array in the minimum number of jumps.",
            "link": "https://leetcode.com/problems/jump-game-ii/description/?envType=problem-list-v2&envId=dynamic-programming"
        },
              {
            "title": "Word Break",
            "difficulty": "Medium", 
            "description": "Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.",
            "link": "https://leetcode.com/problems/word-break/description/?envType=problem-list-v2&envId=dynamic-programming"
        },
               {
            "title": "Merge Intervals",
            "difficulty": "Medium", 
            "description": "Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.",
            "link": "https://leetcode.com/problems/merge-intervals/description/?envType=problem-list-v2&envId=sorting"
        },
                {
            "title": " Contains Duplicate",
            "difficulty": "Medium", 
            "description": "Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.",
            "link": "https://leetcode.com/problems/contains-duplicate/description/?envType=problem-list-v2&envId=sorting"
        },
                 {
            "title": " Unique Binary Search Trees II",
            "difficulty": "Medium", 
            "description": "Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.",
            "link": "https://leetcode.com/problems/unique-binary-search-trees-ii/description/?envType=problem-list-v2&envId=binary-search-tree"
        },
                 {
            "title": " Longest Palindrome",
            "difficulty": "Easy", 
            "description": "Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.",
            "link": "https://leetcode.com/problems/longest-palindrome/description/?envType=problem-list-v2&envId=greedy"
        },
                 {
            "title": " Shortest Unsorted Continuous Subarray",
            "difficulty": "Medium", 
            "description": "Given an integer array nums, you need to find one continuous subarray such that if you only sort this subarray in non-decreasing order, then the whole array will be sorted in non-decreasing order.",
            "link": "https://leetcode.com/problems/shortest-unsorted-continuous-subarray/description/?envType=problem-list-v2&envId=greedy"
        },
                 {
            "title": " Monotone Increasing Digits",
            "difficulty": "Medium", 
            "description": "An integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x <= y. Given an integer n, return the largest integer with monotone increasing digits that is less than or equal to n.",
            "link": "https://leetcode.com/problems/monotone-increasing-digits/description/?envType=problem-list-v2&envId=greedy"
        },




    ]
    day = datetime.datetime.now().timetuple().tm_yday
    return jsonify(problems[day % len(problems)])


    
  # --- 1. המילון (חייב להיות ראשון) ---
LEETCODE_HINTS = {
    "Two Sum": "Use a Hash Map to store numbers: {value: index}. Check if (target - num) exists.",
    "Valid Parentheses": "Use a Stack. Push opening brackets, pop matching closing brackets.",
    "Climbing Stairs": "Dynamic Programming! Steps[i] = Steps[i-1] + Steps[i-2].",
    "Roman to Integer": "If a value is smaller than the next one, subtract it. Otherwise, add it.",
    "Longest Palindrome": "Count letter frequencies. Use all even counts + one odd center.",
    "Longest Substring Without Repeating Characters": "Use a Sliding Window with a Set to track unique characters.",
    "Maximum Subarray": "Kadane's Algorithm: at each step, decide whether to extend the sum or restart.",
    "Group Anagrams": "Sort each string to use as a key in a Hash Map.",
    "Construct Binary Tree from Inorder and Postorder Traversal": "Last element of Postorder is the Root. Find it in Inorder to split left/right.",
    "Copy List with Random Pointer": "Map original nodes to new nodes in a Hash Map, then link pointers.",
    "Fraction to Recurring Decimal": "Use a Hash Map for remainders to detect repeating cycles.",
    "Jump Game II": "Greedy BFS: Jump to the spot that lets you reach the furthest next point.",
    "Word Break": "Dynamic Programming: dp[i] is true if s[0...i] can be split into words.",
    "Merge Intervals": "Sort by start time. Merge if the current interval overlaps with the previous one.",
    "Contains Duplicate": "Use a Hash Set for O(1) lookups to see if a number appeared before.",
    "Unique Binary Search Trees II": "Recursion: Try every number as a root and recursively build left/right subtrees.",
    "Shortest Unsorted Continuous Subarray": "Compare the array with a sorted version of itself.",
    "Monotone Increasing Digits": "Find the first dip in digits, decrease the previous digit, and set the rest to 9."
}

# --- 2. הפונקציה (חייבת להיות אחרי המילון) ---
@app.route('/api/hint', methods=['POST'])
def get_hint():
    data = request.json
    # קבלת הכותרת וניקוי רווחים מיותרים
    problem_title = data.get('title', '').strip()
    
    # חיפוש במילון שהגדרנו למעלה
    hint = LEETCODE_HINTS.get(problem_title, "No hint available yet for this problem. Try breaking it down!")
    
    return jsonify({"hint": hint})

@app.route('/api/chat', methods=['POST'])
#chatbot endpoint
def chat_agent():
    
    user_message = request.json.get('message', '').lower()
    
    response = RESUME_DATA["default"]
    
    if any(word in user_message for word in ["gpa", "grade", "score", "average", "marks", "100"]):
        response = RESUME_DATA["grades"]
    
    elif any(word in user_message for word in ["experience", "idf", "army", "work", "job", "commander", "9900"]):
        response = RESUME_DATA["experience"]
    
    elif any(word in user_message for word in ["skill", "python", "c++", "stack", "technology", "know", "tools"]):
        response = RESUME_DATA["skills"]
    
    elif any(word in user_message for word in ["project", "portfolio", "app", "build", "mouse", "vision"]):
        response = RESUME_DATA["projects"]
    
    elif any(word in user_message for word in ["contact", "email", "phone", "reach", "call"]):
        response = RESUME_DATA["contact"]
        
    elif any(word in user_message for word in ["hire", "why", "strength", "good", "talent", "best"]):
        response = RESUME_DATA["strengths"]
        
    elif any(word in user_message for word in ["goal", "future", "looking", "position", "role"]):
        response = RESUME_DATA["goals"]
        
    elif any(word in user_message for word in ["hobby", "fun", "free", "time", "personal", "life"]):
        response = RESUME_DATA["hobbies"]
        
    elif any(word in user_message for word in ["start", "available","availability", "when", "now", "time"]):
        response = RESUME_DATA["availability"]
        
    elif any(word in user_message for word in ["hello", "hi", "hey", "start"]):
        response = "Hello! I am ready to answer questions about Kristina's career. Try asking 'Why should we hire her?'"
        
    else:
        response = RESUME_DATA["default"]

    return jsonify({"response": response})

if __name__ == '__main__':
    print("Server is running on http://127.0.0.1:5000")
    app.run(debug=True, port=5000)