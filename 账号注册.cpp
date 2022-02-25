#include <iostream>
#include<string>
#include <cstdlib>
#include <ctime>
using namespace std;
int main(void)
{
	void showmenu();
	showmenu();
	int x = 0;
	string str;
	while (true) {
		cin >> x;
		if (x == 1) {
			cout << "正在注册账号，请输入下列信息。" << endl;
			cout << "请输入用户名：" << endl;
			cin >> str;
			cout << "请输入不含空格的密码：" << endl;
			char arr[20] = { "0" };
			cin >> arr;
			cout << "请再次输入密码：" << endl;
			char array[20] = { "0" };
			cin >> array;
			int num = 0, k = 0, sum = 0, p = 0, m = 0, n = 0;



			while (strlen(arr) != strlen(array)) {
				cout << "密码位数不一致，请再次输入密码：" << endl;
				cin >> array;
				m++;
				if (m == 3) {
					cout << "操作过于频繁，请稍后再进行尝试！" << endl;
					return 0;
					//break;
				}
			};


			if (strlen(arr) == strlen(array)) {
				for (int i = 0; i < strlen(arr); i++)
					if (arr[i] == array[i])
						k++;
				while (k != strlen(arr)) {
					cout << "密码不一致，请再次输入密码：" << endl;
					cin >> array;
					n++;
					if (n == 3) {
						cout << "操作过于频繁，请稍后再进行尝试！" << endl;
						return 0;
						//break;
					}
				};


				srand((int)time(0));
				num = 999 + rand() % 999;//获取验证码
				cout << "您的验证码为：" << num << "，请勿告诉他人。" << endl;
				cout << "请输入验证码：" << endl;
				cin >> sum;
				if (sum != num) {
					while (sum != num) {
						if (p == 3) {
							cout << "操作过于频繁，请稍后再进行尝试！" << endl;
							return 0;
							break;
						}
						cout << "验证码错误，请重新填写验证码。" << endl;
						p++;

						cin >> sum;
					}
				}
				else {
					cout << "恭喜您注册成功！请登录您的账号。" << endl;
					break;
				}
			}
		}


		else {
			cout << "欢迎下次使用。" << endl;
			break;
		}
	}
}
void showmenu()
{
	cout << "********欢迎来到理工超市*********" << endl;
	cout << "********1、注册账户**************" << endl;
	cout << "********0、退出系统**************" << endl;
	cout << "*********************************" << endl;
}
