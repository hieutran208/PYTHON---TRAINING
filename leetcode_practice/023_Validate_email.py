"""
Input: 
users = [
        [1, "Winston", "winston@leetcode.com"],
        [2, "Jonathan", "jonathanisgreat"],
        [3, "Annabelle", "bella-@leetcode.com"],
        [4, "Sally", "sally.come@leetcode.com"],
        [5, "Marwan", "quarz#2020@leetcode.com"],
        [6, "David", "david69@gmail.com"],
        [7, "Shapiro", ".shapo@leetcode.com"]
    ]
Output: 
+---------+-----------+-------------------------+
| user_id | name      | mail                    |
+---------+-----------+-------------------------+
| 1       | Winston   | winston@leetcode.com    |
| 3       | Annabelle | bella-@leetcode.com     |
| 4       | Sally     | sally.come@leetcode.com |
+---------+-----------+-------------------------+
"""
import pandas
def validate_emails (users):
    df = pandas.DataFrame(users, columns=['id','name','email'])
    df_filter = df['email'].str.match(r'^[A-Za-z][A-Za-z0-9_.-]*@leetcode\.com$')
    """
    - str.contains khác với str.match: 
        + str.contains: Kiểm tra xem có ký tự cần tìm ở bất kỳ vị trí nào trong chuỗi không
        + str.match: Kiểm tra xem chuỗi có bắt đầu bằng ký tự cần tìm không (= regex có ^ ở đầu)
    - ^ và $: Bắt đâu, kết thúc chuỗi
    - [A-Za-z]: Ký tự đầu tiên là chữ cái ([A-Za-z] nghĩa là a-z hoặc A-Z)
    - [A-Za-z0-9_.-]*: sau đó có thể có nhiều ký tự chữ, số, dấu gạch dưới _, dấu chấm ., hoặc dấu gạch ngang -. 
    (* nghĩa là 0 hoặc nhiều lần)
    - @leetcode\.com: Bắt buộc phải có @leetcode.com 
    (\. để định nghĩa ký tự chấm, vì trong regex nếu chỉ . có nghĩa là “bất kỳ ký tự nào”)
    """
    return  df[df_filter]
if __name__ == '__main__':
    users = [
        [1, "Winston", "winston@leetcode.com"],
        [2, "Jonathan", "jonathanisgreat"],
        [3, "Annabelle", "bella-@leetcode.com"],
        [4, "Sally", "sally.come@leetcode.com"],
        [5, "Marwan", "quarz#2020@leetcode.com"],
        [6, "David", "david69@gmail.com"],
        [7, "Shapiro", ".shapo@leetcode.com"]
    ]
    print(validate_emails(users))