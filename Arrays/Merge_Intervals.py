# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

# You may assume that the intervals were initially sorted according to their start times.

# Example 1:

# Given intervals [1,3],[6,9] insert and merge [2,5] would result in [1,5],[6,9].

# Example 2:

# Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] would result in [1,2],[3,10],[12,16].

# This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

# Make sure the returned intervals are also sorted.

##########################################################################################################################################

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, new_interval):
        
        if new_interval.start > new_interval.end:
            tmp = (new_interval.end, new_interval.start)
            new_interval = tmp
        
        if len(intervals) == 0:
            intervals.append(new_interval)
            return intervals
        elif new_interval.end < intervals[0].start:
            tmp = []
            tmp.append(new_interval)
            tmp.extend(intervals)
            return tmp
        elif intervals[-1].end < new_interval.start:
            intervals.append(new_interval)
            return intervals
        elif new_interval.start <= intervals[0].start and new_interval.end >= intervals[-1].end:
            tmp = []
            tmp.append(new_interval)
            return tmp
        
        s_idx = 0
        s_side = 0
        b_idx = 0
        b_side = 0
        for ii in range(len(intervals)):
            if new_interval.start <= intervals[ii].start:
                s_idx = ii
                s_side = 0
                break
            elif new_interval.start <= intervals[ii].end:
                s_idx = ii
                s_side = 1
                break
            
        for ii in range(len(intervals) - 1, -1, -1):
            if new_interval.end >= intervals[ii].end:
                b_idx = ii
                b_side = 1
                break
            elif new_interval.end >= intervals[ii].start:
                b_idx = ii
                b_side = 0
                break
        
        new_list = []
        new_list.extend(intervals[:s_idx])
        if s_side == 0 and b_side == 0:
            new_interval.end = intervals[b_idx].end
            new_list.append(new_interval)
            new_list.extend(intervals[b_idx+1:])
        elif s_side == 0 and b_side == 1:
            new_list.append(new_interval)
            new_list.extend(intervals[b_idx+1:])
        elif s_side == 1 and b_side == 0:
            new_interval.start = intervals[s_idx].start
            new_interval.end = intervals[b_idx].end
            new_list.append(new_interval)
            new_list.extend(intervals[b_idx+1:])
        else:
            new_interval.start = intervals[s_idx].start
            new_list.append(intervals[s_idx].start, new_interval.end)
            new_list.extend(intervals[b_idx+1:])
        
        return new_list
            
##########################################################################################################################################
