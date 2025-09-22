# 本文件为简单的quaternion类，以供ipynb使用
import numpy as np
import math

# Quaternion类
# 1. 初始化为单位四元数q，其中第一个参数为实部，后三个参数为虚部

class Quaternion:
    def __init__(self, w, x, y, z):
        """
        初始化四元数
        :param w: 实部
        :param x: 虚部 i 的系数
        :param y: 虚部 j 的系数
        :param z: 虚部 k 的系数
        """
        self.w = w
        self.x = x
        self.y = y
        self.z = z
        
        
    @classmethod
    def from_vector_angle(self, v, angle):
        """
        从向量-角表示创建四元数
        :param v: 四元数的虚部，必须是单位向量
        :param angle: 角度，单位为弧度
        :return: 对应的四元数
        """
        sin_angle = math.sin(angle)
        w = math.cos(angle)
        x = v[0] * sin_angle
        y = v[1] * sin_angle
        z = v[2] * sin_angle
        return self(w, x, y, z)

    def __str__(self):
        """
        返回四元数的字符串表示
        """
        return f"Quaternion({self.w}, {self.x}, {self.y}, {self.z})"

    def __add__(self, other):
        """
        四元数加法
        :param other: 另一个四元数
        :return: 相加后的四元数
        """
        if isinstance(other, Quaternion):
            return Quaternion(self.w + other.w, self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            raise TypeError("Unsupported operand type for +: 'Quaternion' and '{}'".format(type(other).__name__))

    def __mul__(self, other):
        """
        四元数乘法
        :param other: 另一个四元数或标量
        :return: 相乘后的四元数
        """
        if isinstance(other, Quaternion):
            w = self.w * other.w - self.x * other.x - self.y * other.y - self.z * other.z
            x = self.w * other.x + self.x * other.w + self.y * other.z - self.z * other.y
            y = self.w * other.y - self.x * other.z + self.y * other.w + self.z * other.x
            z = self.w * other.z + self.x * other.y - self.y * other.x + self.z * other.w
            return Quaternion(w, x, y, z)
        elif isinstance(other, (int, float)):
            return Quaternion(self.w * other, self.x * other, self.y * other, self.z * other)
        else:
            raise TypeError("Unsupported operand type for *: 'Quaternion' and '{}'".format(type(other).__name__))

    def conjugate(self):
        """
        四元数的共轭
        :return: 共轭后的四元数
        """
        return Quaternion(self.w, -self.x, -self.y, -self.z)

    def norm(self):
        """
        四元数的模
        :return: 四元数的模
        """
        return math.sqrt(self.w ** 2 + self.x ** 2 + self.y ** 2 + self.z ** 2)

    def normalize(self):
        """
        四元数归一化
        :return: 归一化后的四元数
        """
        n = self.norm()
        if n == 0:
            raise ValueError("Cannot normalize a quaternion with norm 0.")
        return Quaternion(self.w / n, self.x / n, self.y / n, self.z / n)
    
    def as_numpy(self):
        """
        将四元数转换为numpy数组
        :return: numpy数组表示的四元数
        """
        return np.array([self.w, self.x, self.y, self.z])
        