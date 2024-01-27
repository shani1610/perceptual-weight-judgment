# Human Perceptual Weight Judgment Dataset

Collaborators: [Georgopoulou, Artemis](https://github.com/artemisge) | [Israelov, Shani](https://github.com/shani1610) | [Izumi, Takerhiro](https://github.com/sytk) | [Manschein, Fabiano](https://github.com/Fabulani) | [Takagi, Yuya](https://github.com/shiohiyoko)

[[Project Report]](https://docs.google.com/document/d/e/2PACX-1vSASPeU8cQC7EI6yIh76JWRZKQWgrYbdHmD1CYblf8ZGva5pHf9cNvCmzJoQ0WjJg73TBcDSSHU6jVA/pub)
<p align="center">
<img src="images/snippet1.png" alt="teaser" width="1920"/>
</p>
This is a dataset for human perceptual weight judgment. 

## Contents
1. [Description](#description)
2. [Download](#download)
3. [Dataset Structure](#dataset-structure)
4. [License](#license)
5. [Citation](#citation)

## Description
The Perceptual Weight Judgment dataset is a dataset of humans lift box with changing weights.
Each subject was asked to lift a box from the ground to a table.
Without letting the subject know, the weight of the carrying box was randomly changed by putting different weight plates into a concealed box, 
ranging from 0 kg to 20 kg with a step of 5 kg.

The dataset includes:

5 subjects interacting with a cocealed box with 5 different weights at neutral environment.
In total 25 video sequences recorded with Iphone.

## Download
For download, please click [here](https://www.dropbox.com/scl/fi/0jrgn887lnpv4cwj3qf4k/data.zip?rlkey=otauddx7u6bhz9cc55qxwmpem&dl=0)

## Dataset Structure
After unzip the dataset, you can find folder `data` containing file with the name `video_wW_aA_cC.MOV` where W is the weight, A is the actor numeration and C indicate 0/1 for uncropped/cropped image accordingly, for example: `video_w0_a1_c0.MOV` indicates weight 0kg, actor number 1, uncropped image. 

## Example usage
Here we describe example usage of our dataset: 

### Crop 30% of the frame from the bottom 

We provide sample code in `crop_bottom.py` to crop 30% of the frame from the bottom. Run with:
```
python crop_bottom.py -s DATA_PATH
``` 

## License
Copyright (c) 2024, Toyohashi-University-Of-Technology

Please read carefully the following terms and conditions and any accompanying documentation before you download and/or use this software and associated documentation files (the "Software").

The authors hereby grant you a non-exclusive, non-transferable, free of charge right to copy, modify, merge, publish, distribute, and sublicense the Software for the sole purpose of performing non-commercial scientific research, non-commercial education, or non-commercial artistic projects.

Any other use, in particular any use for commercial purposes, is prohibited. This includes, without limitation, incorporation in a commercial product, use in a commercial service, or production of other artefacts for commercial purposes.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

You understand and agree that the authors are under no obligation to provide either maintenance services, update services, notices of latent defects, or corrections of defects with regard to the Software. The authors nevertheless reserve the right to update, modify, or discontinue the Software at any time.

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. You agree to **cite the Dataset for human perceptual weight judgment** data in documents and papers that report on research using this Software.

In case the images are used for publication or public presentations, you are required to <strong>blur all human faces</strong>.

## Citation
If you use our code or data, please cite:
```bibtex
@inproceedings{liftingbox2024,
  title={Dataset for human perceptual weight judgment},
  author={Georgopoulou, Artemis and Israelov, Shani and Izumi, Takerhiro and Manschein, Fabiano and Takagi, Yuya}
  year={2024}
}
```
