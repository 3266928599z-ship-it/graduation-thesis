# graduation-thesis

面向焊接机器人的三维点云免示教焊接系统 —— 硕士学位论文开题答辩资料。

## 仓库内容

| 路径 | 说明 |
|---|---|
| `文献清单-汇总.md` | 开题答辩文献清单总表（中文 11 + 外文 18，含去重、核心精读优先级、待补元数据） |
| `文献综述-补充文献清单.md` | 文献综述补充清单（按配准/粗配准/精配准/深度学习/焊接视觉分类） |
| `文献PDF/` | 已下载的参考文献原文 PDF（9 篇） |

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
