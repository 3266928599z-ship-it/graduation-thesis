# graduation-thesis

面向焊接机器人的三维点云免示教焊接系统 —— 硕士学位论文开题答辩资料。

## 仓库内容

| 路径 | 说明 |
|---|---|
| `文献清单-汇总.md` | 开题答辩文献清单总表（中文 10 + 外文 18，含去重、核心精读优先级、已补全元数据） |
| `文献综述-补充文献清单.md` | 文献综述补充清单（按配准/粗配准/精配准/深度学习/焊接视觉分类） |
| `文献PDF/` | 已下载的英文参考文献原文 PDF（9 篇） |
| `文献/` | 已下载的中文参考文献原文 PDF（10 篇） |

## 研究主题

- **课题**：面向焊接机器人的三维点云免示教焊接系统
- **技术路线**：点云配准（PCA/FPFH/PPF 粗配准 + 多级裁剪 ICP 精配准）→ 配准质量多维自动判定 → 基于 CAD 面求交的焊缝提取
- **技术栈**：C++ / Qt6 / PCL / OpenCascade / Eigen / VTK / 海康 MVS SDK

## 参考文献 PDF 清单（`文献PDF/`）

| 文件 | 内容 |
|---|---|
| `Aoki2019_PointNetLK.pdf` | PointNetLK: Robust & efficient point cloud registration using PointNet |
| `Huang2021_点云配准综述.pdf` | A comprehensive survey on point cloud registration |
| `Low2004_点到面ICP线性求解.pdf` | Linear least-squares optimization for point-to-plane ICP |
| `Mellado2014_Super4PCS.pdf` | Super 4PCS: Fast global pointcloud registration via smart indexing |
| `Segal2009_GICP.pdf` | Generalized-ICP |
| `Wang2019_DCP.pdf` | Deep Closest Point: Learning representations for point cloud registration |
| `Yang2020_TEASER.pdf` | TEASER: Fast and certifiable point cloud registration |
| `Yew2020_RPM-Net.pdf` | RPM-Net: Robust point matching using learned features |
| `Zhou2016_FGR.pdf` | Fast global registration |

## 中文文献 PDF 清单（`文献/`）

| 文件 | 内容 |
|---|---|
| `基于面结构光的焊缝坡口特征提取_余明岭.pdf` | 组合机床与自动化加工技术, 2023(12): 17-20 |
| `基于3D点云的焊缝识别和路径规划研究_郭丽红.pdf` | 物联网技术, 2024(12): 145-148 |
| `基于点云数据驱动的中厚板机器人焊接路径规划_李秉聪.pdf` | 电焊机, 2023, 53(9): 78-83 |
| `基于3D点云的平面角接焊缝特征提取与运动跟踪_吴海彬.pdf` | 东北大学学报(自然科学版), 2025, 46(6): 1-9 |
| `基于点云特征提取的V型焊缝焊接系统研究_王凯.pdf` | 中国计量大学硕士论文, 2019 |
| `基于点云的机器人焊缝自动化磨削系统与方法_葛吉民.pdf` | 中国机械工程, 2024, 35(7): 1253-1262 |
| `面向焊接机器人的视觉传感技术_程进.pdf` | 电焊机, 2023, 53(9): 61-69 |
| `焊接机器人视觉感知及智能化焊接关键技术研究进展_陈华斌.pdf` | 焊接学报, 2024(11): 1-9 |
| `机器视觉辅助机器人焊接全过程研究进展_高振泽.pdf` | 电焊机, 2025, 55(9): 1-18 |
| `机器人智能化焊接技术发展综述_刘少意.pdf` | 金属加工(热加工), 2025(6): 1-12 |
