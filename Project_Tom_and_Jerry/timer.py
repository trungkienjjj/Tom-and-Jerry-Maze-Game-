
'''
import time
class Clock:
    def __init__(self):
        self.start_time = None

    def start(self):
        """Bắt đầu đếm thời gian"""
        self.start_time = time.time()
        
    def get_elapsed_time(self):
        """Trả về thời gian đã trôi qua kể từ lúc bắt đầu"""
        if self.start_time is None:
            raise ValueError("Đồng hồ chưa được bắt đầu")
        elapsed_time = time.time() - self.start_time
        return elapsed_time

'''

import time

class Clock:
    def __init__(self):
        self.start_time = None
        self.paused_time = None
        self.elapsed_time = 0.0

    def start(self, elapsed_time=0.0):
        """Bắt đầu đếm thời gian từ thời điểm hiện tại hoặc từ thời gian đã cho"""
        self.start_time = time.time()
        self.paused_time = None
        self.elapsed_time = elapsed_time
        
    def get_elapsed_time(self):
        """Trả về thời gian đã trôi qua kể từ lúc bắt đầu"""
        if self.start_time is None:
            raise ValueError("Đồng hồ chưa được bắt đầu")
        if self.paused_time is not None:
            return self.elapsed_time
        return time.time() - self.start_time + self.elapsed_time

    def pause(self):
        """Tạm ngưng đồng hồ"""
        if self.start_time is None:
            raise ValueError("Đồng hồ chưa được bắt đầu")
        if self.paused_time is None:
            self.paused_time = time.time()
            self.elapsed_time += self.paused_time - self.start_time
        
    def continue_(self):
        """Tiếp tục tính thời gian từ lúc nhấn pause"""
        if self.paused_time is None:
            raise ValueError("Đồng hồ chưa được tạm ngưng")
        self.start_time = time.time()
        self.paused_time = None
    
    

