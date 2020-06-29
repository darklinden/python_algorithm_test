#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import sys

from base import Solution


class BinaryCut(Solution):

    def algorithm_func(self, nums1: list, nums2: list) -> float:

        n_short = len(nums1)
        n_long = len(nums2)

        if n_short > n_long:
            return self.algorithm_func(nums2, nums1)

        # 二分法区间
        bc_low = 0
        bc_high = n_short

        # 计算用于从short分割线位置i获取long分割线位置j的总和的半长
        n_half = int(math.floor((n_short + n_long) / 2))
        if (n_short + n_long) % 2 != 0:
            # 当奇数总长时，保证左边部分比右边部分多一个元素
            n_half += 1

        INT_MAX: int = sys.maxsize
        INT_MIN: int = -sys.maxsize - 1

        # 短数组的切面左侧值和长数组的切面右侧值组成最终结果
        c_l = INT_MIN
        c_r = INT_MIN
        c_short_l = 0
        c_short_r = 0
        c_long_l = 0
        c_long_r = 0

        left = []
        right = []

        # 二分法搜索区间
        while True:
            if bc_low > bc_high:
                # print('bc_low: ' + str(bc_low) + ' > bc_high: ' + str(bc_high))
                break
            mid = int(math.floor((bc_high - bc_low) / 2))
            i = bc_low + mid
            j = n_half - i

            c_short_l = INT_MIN if i == 0 else nums1[i - 1]
            c_short_r = INT_MAX if i == len(nums1) else nums1[i]
            c_long_l = INT_MIN if j == 0 else nums2[j - 1]
            c_long_r = INT_MAX if j == len(nums2) else nums2[j]

            # print('')
            # print('nums1 index: ' + str(i))
            # print(str(nums1[(i - 10):i]) + ' - ' + str(nums1[i:(i + 10)]))
            #
            # print('nums2 index: ' + str(j))
            # print(str(nums2[(j - 10):j]) + ' - ' + str(nums2[j:(j + 10)]))
            #
            # left = nums1[:i] + nums2[:j]
            # right = nums1[i:] + nums2[j:]
            # print('left  len: ' + str(len(left)) + ' - ...' + str(sorted(left)[-10:]))
            # print('right len: ' + str(len(right)) + ' - ' + str(sorted(right)[:10]) + '...')

            if max(c_short_l, c_long_l) <= min(c_short_r, c_long_r):
                # 满足条件，直接跳出
                c_l = max(c_short_l, c_long_l)
                c_r = min(c_short_r, c_long_r)
                break
            else:
                # 不满足条件，缩小范围

                if c_short_l > c_long_r:
                    # 如果nums1的分割线左侧过大，减小上限以降低中值

                    # 降低二分上限
                    bc_high = i + (mid / 2)

                else:
                    # 否则，减小二分上限以缩小范围

                    # 提升二分下限
                    bc_low = i + 1

        # 处理循环跳出仍未满足条件
        assert c_l != INT_MIN and c_r != INT_MIN

        # print(max(left)) if len(left) > 0 else print('None')
        # print(min(right)) if len(right) > 0 else print('None')

        return (c_l + c_r) / 2.0 if (n_long + n_short) % 2 == 0 else min(c_l, c_r)


def main():
    test_case_list = [
        {
            'test_args': {'nums1': [3], 'nums2': [-2, -1]},
            'expect_val': {'ret_val': -1},
            'comment': '负数'
        },
        {
            'test_args': {'nums1': [], 'nums2': [1]},
            'expect_val': {'ret_val': 1},
            'comment': '空集'
        },

        {
            'test_args': {
                'nums1': [103, 360, 400, 444, 448, 484, 492, 598, 626, 661, 688, 745, 759, 769, 816, 859, 871, 1003,
                          1006, 1099, 1119, 1213, 1234, 1320, 1434, 1490, 1517, 1659, 1708, 1752, 1872, 1880, 1883,
                          1892, 1923, 1951, 1955, 2039, 2041, 2139, 2250, 2334, 2373, 2382, 2385, 2391, 2400, 2406,
                          2542, 2558, 2577, 2751, 2782, 2812, 2873, 2885, 2889, 3059, 3127, 3140, 3181, 3368, 3661,
                          3766, 3782, 3797, 3861, 3883, 3955, 3958, 3969, 4004, 4066, 4354, 4383, 4441, 4450, 4463,
                          4511, 4547, 4647, 4707, 4757, 4793, 4794, 4825, 5017, 5033, 5059, 5183, 5236, 5238, 5289,
                          5336, 5373, 5654, 5913, 6045, 6102, 6114, 6120, 6210, 6279, 6285, 6327, 6432, 6498, 6503,
                          6547, 6548, 6554, 6708, 6719, 6744, 6801, 6878, 6944, 6986, 7039, 7138, 7146, 7250, 7341,
                          7355, 7369, 7386, 7432, 7489, 7526, 7591, 7619, 7659, 7790, 7805, 7828, 7878, 7900, 7914,
                          7998, 8078, 8080, 8505, 8510, 8604, 8618, 8636, 8666, 8785, 8832, 8894, 8903, 8914, 8920,
                          8923, 9024, 9039, 9050, 9059, 9066, 9083, 9151, 9161, 9203, 9245, 9367, 9515, 9530, 9540,
                          9559, 9649, 9726, 9757, 9816, 9819, 9849, 9870, 9876, 9883, 9908, 9941, 10010, 10019, 10170,
                          10301, 10344, 10351, 10398, 10409, 10450, 10461, 10495, 10693, 10706, 10719, 10850, 10885,
                          10955, 10957, 10993, 11090, 11116, 11124, 11192, 11205, 11310, 11473, 11551, 11565, 11736,
                          11763, 11792, 12006, 12109, 12148, 12214, 12217, 12265, 12310, 12329, 12384, 12435, 12452,
                          12459, 12501, 12543, 12566, 12637, 12669, 12875, 12884, 13019, 13055, 13062, 13077, 13117,
                          13117, 13119, 13123, 13138, 13146, 13218, 13251, 13257, 13266, 13448, 13489, 13560, 13616,
                          13637, 13673, 13750, 13802, 13825, 13833, 13857, 13907, 13953, 13984, 13990, 14056, 14059,
                          14078, 14081, 14093, 14112, 14128, 14160, 14191, 14227, 14272, 14275, 14381, 14425, 14431,
                          14550, 14614, 14744, 14765, 14765, 14796, 14820, 14863, 14863, 14903, 14916, 14937, 14990,
                          15022, 15039, 15107, 15128, 15166, 15193, 15205, 15213, 15271, 15299, 15329, 15374, 15484,
                          15539, 15557, 15614, 15616, 15655, 15701, 15707, 15733, 15768, 15862, 16053, 16096, 16165,
                          16167, 16174, 16235, 16242, 16253, 16273, 16294, 16302, 16360, 16367, 16381, 16575, 16598,
                          16659, 16674, 16701, 16707, 16781, 16799, 16807, 16978, 17240, 17272, 17299, 17363, 17395,
                          17562, 17587, 17727, 17750, 17825, 17859, 17918, 17923, 17930, 17933, 18009, 18047, 18052,
                          18150, 18236, 18253, 18271, 18353, 18432, 18459, 18507, 18527, 18528, 18571, 18608, 18647,
                          18662, 18735, 18750, 18812, 18812, 18876, 19052, 19075, 19109, 19135, 19212, 19247, 19393,
                          19500, 19502, 19529, 19578, 19758, 19773, 19802, 19880, 19903, 19943, 20064, 20211, 20217,
                          20252, 20288, 20361, 20389, 20407, 20419, 20502, 20601, 20782, 20791, 20891, 21038, 21043,
                          21073, 21247, 21441, 21447, 21464, 21513, 21522, 21575, 21700, 21724, 21803, 21864, 21929,
                          22041, 22044, 22098, 22163, 22211, 22226, 22235, 22244, 22248, 22272, 22406, 22414, 22466,
                          22470, 22630, 22652, 22713, 22767, 22778, 22780, 22817, 22909, 22915, 22928, 23023, 23038,
                          23045, 23050, 23095, 23117, 23162, 23177, 23184, 23268, 23341, 23367, 23373, 23475, 23476,
                          23561, 23726, 23740, 23809, 23942, 23950, 24019, 24037, 24118, 24185, 24189, 24251, 24272,
                          24284, 24293, 24312, 24355, 24362, 24408, 24453, 24464, 24524, 24593, 24662, 24667, 24855,
                          24883, 24947, 25044, 25096, 25134, 25143, 25295, 25342, 25469, 25484, 25491, 25491, 25497,
                          25527, 25599, 25607, 25617, 25642, 25766, 25785, 25791, 25792, 25894, 25903, 25959, 26055,
                          26090, 26131, 26229, 26230, 26259, 26270, 26307, 26410, 26460, 26510, 26697, 26734, 26753,
                          26817, 26831, 26845, 26866, 27031, 27156, 27180, 27196, 27293, 27396, 27562, 27681, 27719,
                          27749, 27770, 28090, 28148, 28245, 28304, 28311, 28365, 28373, 28433, 28468, 28470, 28485,
                          28569, 28741, 28746, 28913, 28960, 29041, 29043, 29131, 29192, 29290, 29332, 29355, 29388,
                          29425, 29479, 29538, 29624, 29636, 29652, 29709, 29746, 29766, 29813, 29868, 29926, 29956,
                          30098, 30135, 30149, 30170, 30193, 30236, 30282, 30290, 30351, 30460, 30508, 30519, 30520,
                          30522, 30523, 30533, 30559, 30752, 30815, 30822, 30863, 30882, 30922, 30995, 31036, 31097,
                          31115, 31249, 31285, 31375, 31449, 31580, 31597, 31602, 31605, 31643, 31712, 31845, 31862,
                          31869, 31899, 31923, 31981, 31989, 32116, 32259, 32301, 32318, 32410, 32469, 32493, 32496,
                          32607, 32696, 32699, 32709],
                'nums2': [32, 86, 87, 100, 108, 119, 154, 181, 188, 261, 310, 317, 460, 479, 488, 490, 523, 529, 624,
                          700, 744, 751, 765, 780, 1044, 1048, 1067, 1185, 1231, 1252, 1292, 1327, 1356, 1387, 1411,
                          1442, 1474, 1493, 1498, 1508, 1509, 1542, 1559, 1566, 1634, 1665, 1686, 1711, 1725, 1742,
                          1747, 1799, 1870, 1900, 1925, 1973, 2014, 2050, 2098, 2182, 2223, 2246, 2311, 2331, 2368,
                          2375, 2383, 2386, 2408, 2440, 2453, 2460, 2501, 2512, 2523, 2538, 2542, 2577, 2668, 2676,
                          2713, 2767, 2803, 2819, 2953, 2988, 3071, 3071, 3104, 3198, 3207, 3209, 3271, 3277, 3297,
                          3301, 3303, 3329, 3349, 3349, 3374, 3404, 3437, 3510, 3578, 3622, 3653, 3659, 3674, 3677,
                          3769, 3814, 3924, 3944, 4078, 4161, 4167, 4285, 4318, 4377, 4390, 4414, 4505, 4550, 4554,
                          4556, 4560, 4588, 4588, 4624, 4699, 4714, 4723, 4730, 4777, 4830, 4843, 4883, 4995, 5154,
                          5184, 5189, 5199, 5205, 5213, 5316, 5326, 5331, 5363, 5365, 5369, 5372, 5390, 5390, 5402,
                          5407, 5429, 5444, 5481, 5497, 5501, 5524, 5591, 5639, 5639, 5647, 5661, 5731, 5737, 5780,
                          5864, 5875, 5903, 5913, 5923, 6014, 6043, 6053, 6090, 6105, 6113, 6166, 6184, 6320, 6364,
                          6398, 6432, 6642, 6647, 6664, 6678, 6712, 6726, 6789, 6799, 6822, 6826, 6926, 7034, 7039,
                          7048, 7115, 7126, 7164, 7213, 7273, 7326, 7355, 7479, 7492, 7530, 7553, 7557, 7629, 7629,
                          7736, 7814, 7828, 7854, 8050, 8089, 8149, 8152, 8172, 8190, 8232, 8248, 8379, 8541, 8555,
                          8643, 8652, 8658, 8670, 8730, 8737, 8770, 8804, 8808, 8827, 8895, 8955, 8978, 9144, 9285,
                          9298, 9339, 9406, 9419, 9438, 9457, 9610, 9650, 9652, 9673, 9749, 9807, 9874, 9885, 9914,
                          10000, 10039, 10074, 10099, 10100, 10129, 10133, 10197, 10223, 10230, 10315, 10375, 10382,
                          10407, 10450, 10473, 10559, 10571, 10587, 10596, 10627, 10728, 10741, 10764, 10812, 10842,
                          10877, 10895, 10905, 10914, 10927, 10959, 10976, 11050, 11104, 11136, 11156, 11167, 11209,
                          11212, 11217, 11227, 11297, 11299, 11360, 11374, 11427, 11446, 11535, 11540, 11545, 11558,
                          11642, 11650, 11681, 11744, 11758, 11766, 11776, 11789, 11817, 11949, 11993, 12045, 12095,
                          12113, 12114, 12127, 12223, 12229, 12311, 12322, 12337, 12338, 12403, 12576, 12578, 12606,
                          12612, 12629, 12727, 12728, 12749, 12767, 12851, 12890, 12893, 12925, 12940, 12954, 13082,
                          13161, 13188, 13251, 13270, 13273, 13321, 13349, 13360, 13445, 13475, 13521, 13550, 13573,
                          13608, 13619, 13630, 13690, 13701, 13743, 13799, 13814, 13865, 13877, 13883, 14008, 14070,
                          14143, 14158, 14171, 14175, 14192, 14207, 14220, 14347, 14371, 14396, 14411, 14472, 14473,
                          14489, 14522, 14552, 14611, 14624, 14626, 14644, 14697, 14702, 14779, 14834, 14846, 14849,
                          14888, 14970, 14981, 15040, 15119, 15245, 15265, 15321, 15355, 15426, 15437, 15522, 15532,
                          15533, 15563, 15624, 15652, 15671, 15727, 15749, 15894, 15947, 16006, 16013, 16026, 16063,
                          16156, 16185, 16269, 16311, 16345, 16350, 16357, 16434, 16457, 16458, 16460, 16496, 16507,
                          16596, 16637, 16642, 16767, 16770, 16823, 16836, 16842, 16932, 17000, 17022, 17081, 17098,
                          17130, 17147, 17228, 17265, 17312, 17429, 17460, 17549, 17554, 17578, 17605, 17671, 17675,
                          17699, 17701, 17703, 17712, 17728, 17771, 17805, 17850, 17907, 17923, 17923, 17930, 18035,
                          18043, 18069, 18086, 18128, 18179, 18180, 18193, 18219, 18227, 18232, 18251, 18255, 18275,
                          18338, 18349, 18367, 18372, 18380, 18390, 18456, 18460, 18508, 18541, 18550, 18570, 18571,
                          18575, 18682, 18701, 18740, 18753, 18762, 18825, 18850, 18895, 18984, 19027, 19029, 19043,
                          19054, 19060, 19113, 19175, 19205, 19210, 19220, 19226, 19253, 19257, 19290, 19304, 19320,
                          19332, 19355, 19366, 19394, 19416, 19417, 19429, 19442, 19478, 19517, 19521, 19540, 19559,
                          19562, 19586, 19594, 19622, 19630, 19647, 19658, 19662, 19717, 19721, 19786, 19823, 19841,
                          19844, 19874, 19876, 19919, 20006, 20016, 20052, 20087, 20105, 20148, 20159, 20207, 20221,
                          20259, 20262, 20268, 20270, 20282, 20347, 20375, 20377, 20427, 20463, 20499, 20500, 20532,
                          20534, 20555, 20596, 20604, 20620, 20628, 20634, 20699, 20729, 20748, 20774, 20816, 20841,
                          20863, 20943, 20984, 21109, 21135, 21183, 21205, 21351, 21369, 21371, 21373, 21388, 21451,
                          21460, 21538, 21584, 21610, 21611, 21619, 21620, 21733, 21769, 21783, 21803, 21829, 21852,
                          21859, 21907, 21924, 21933, 22049, 22056, 22073, 22098, 22104, 22218, 22232, 22266, 22276,
                          22364, 22377, 22393, 22428, 22452, 22455, 22461, 22494, 22498, 22532, 22551, 22566, 22578,
                          22580, 22587, 22644, 22649, 22679, 22726, 22727, 22736, 22743, 22753, 22781, 22806, 22849,
                          22852, 22873, 22910, 22924, 22976, 23012, 23051, 23069, 23090, 23099, 23112, 23114, 23134,
                          23162, 23177, 23192, 23206, 23232, 23253, 23271, 23288, 23289, 23329, 23352, 23359, 23362,
                          23373, 23384, 23446, 23469, 23485, 23502, 23509, 23547, 23555, 23569, 23583, 23607, 23694,
                          23702, 23706, 23760, 23771, 23802, 23811, 23866, 23886, 23914, 23942, 23975, 24054, 24100,
                          24122, 24156, 24190, 24194, 24200, 24205, 24279, 24296, 24300, 24304, 24329, 24369, 24386,
                          24422, 24435, 24457, 24471, 24481, 24489, 24515, 24529, 24532, 24568, 24640, 24652, 24654,
                          24679, 24713, 24717, 24761, 24790, 24967, 24979, 24982, 25058, 25154, 25230, 25246, 25271,
                          25272, 25289, 25335, 25347, 25392, 25393, 25426, 25487, 25691, 25718, 25720, 25768, 25768,
                          25843, 25864, 25881, 25924, 25957, 25974, 25981, 26099, 26139, 26142, 26194, 26208, 26254,
                          26270, 26307, 26346, 26346, 26353, 26392, 26506, 26519, 26528, 26628, 26654, 26748, 26818,
                          26864, 26869, 26984, 27060, 27105, 27125, 27213, 27222, 27245, 27306, 27337, 27340, 27344,
                          27451, 27454, 27568, 27595, 27609, 27632, 27646, 27657, 27761, 27796, 27835, 27884, 27896,
                          27991, 27997, 28021, 28049, 28139, 28141, 28143, 28194, 28231, 28281, 28296, 28413, 28418,
                          28477, 28483, 28485, 28562, 28588, 28676, 28699, 28791, 28803, 28821, 28852, 28908, 28972,
                          28975, 28995, 29034, 29085, 29104, 29196, 29223, 29248, 29272, 29304, 29307, 29348, 29433,
                          29442, 29508, 29558, 29579, 29594, 29702, 29740, 29748, 29775, 29797, 29818, 29875, 29954,
                          29975, 29985, 29997, 30015, 30086, 30117, 30197, 30204, 30242, 30246, 30263, 30279, 30296,
                          30322, 30393, 30415, 30424, 30436, 30446, 30447, 30480, 30516, 30530, 30532, 30547, 30551,
                          30584, 30632, 30639, 30683, 30743, 30748, 30750, 30757, 30771, 30802, 30827, 30872, 30948,
                          30977, 31050, 31054, 31110, 31150, 31169, 31190, 31191, 31199, 31238, 31290, 31311, 31330,
                          31374, 31395, 31409, 31431, 31446, 31473, 31553, 31562, 31607, 31627, 31630, 31708, 31806,
                          31819, 31843, 31896, 31996, 32000, 32041, 32060, 32111, 32189, 32277, 32343, 32348, 32359,
                          32385, 32391, 32407, 32489, 32496, 32523]},
            'expect_val': {'ret_val': 17234.0},
            'comment': '长'
        },
        {
            'test_args': {'nums1': [1, 2, 3, 7, 8], 'nums2': [4, 5, 6, 9, 10]},
            'expect_val': {'ret_val': 5.5},
            'comment': '奇数奇数'
        },

        {
            'test_args': {'nums1': [1, 2], 'nums2': [1, 1]},
            'expect_val': {'ret_val': 1.0},
            'comment': '偶数偶数'
        },
        {
            'test_args': {'nums1': [1, 1], 'nums2': [1, 2]},
            'expect_val': {'ret_val': 1.0},
            'comment': '同同'
        },
        {
            'test_args': {'nums1': [1, 2], 'nums2': [3]},
            'expect_val': {'ret_val': 2.0},
            'comment': '12，3'
        },
        {
            'test_args': {'nums1': [1, 3], 'nums2': [2]},
            'expect_val': {'ret_val': 2.0},
            'comment': '13，2'
        },
        {
            'test_args': {'nums1': [1, 3], 'nums2': [2, 4]},
            'expect_val': {'ret_val': 2.5},
            'comment': '13，24'
        },
        {
            'test_args': {'nums1': [1, 3, 5, 7, 9], 'nums2': [2, 4, 6, 8]},
            'expect_val': {'ret_val': 5.0},
            'comment': '长奇短偶'
        },
        {
            'test_args': {'nums1': [1, 3, 5, 7, 9], 'nums2': [2, 4, 6, 8, 10, 12]},
            'expect_val': {'ret_val': 6.0},
            'comment': '长偶短奇'
        },
        {
            'test_args': {'nums1': [1, 2, 3, 4, 5], 'nums2': [10, 11, 12, 13]},
            'expect_val': {'ret_val': 5.0},
            'comment': '长小短大'
        },
        {
            'test_args': {'nums1': [1, 2, 3, 4], 'nums2': [10, 11, 12, 13, 14]},
            'expect_val': {'ret_val': 10.0},
            'comment': '长大短小'
        },
    ]

    ins = BinaryCut()
    for t in test_case_list:
        ins.test(**t)


if __name__ == "__main__":
    main()
