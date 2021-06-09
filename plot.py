import matplotlib.pyplot as plt

m = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
su0 = [0.04, 0.49, 0.73, 0.89, 0.92, 0.97, 0.99, 0.99, 1.0, 1.0]
su1 = [0.04, 0.29, 0.65, 0.79, 0.91, 0.97, 0.98, 0.99, 0.99, 1.0]
su2 = [0.0, 0.02, 0.1, 0.21, 0.29, 0.41, 0.5, 0.61, 0.58, 0.65]


plt.title("RC4 attack") 
plt.xlabel("Message volume") 
plt.ylabel("Success rate") 

plt.plot(m, su0, marker='o', markersize=3)  # 绘制折线图，添加数据点，设置点的大小
plt.plot(m, su1, marker='o', markersize=3)
plt.plot(m, su2, marker='o', markersize=3)

for a, b in zip(m, su0):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)  # 设置数据标签位置及大小
for a, b in zip(m, su1):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
for a, b in zip(m, su2):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)

plt.legend(['pass!', 'passw0rd', 'wep_passw0rd!'])  # 设置折线名称

plt.show()



