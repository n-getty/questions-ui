# AuroraGPT AI Model Evaluation Platform

A form to author and review MCQ for LLMs for evaluation, and to perform LabStyle experiments for LLMs for scientific use cases.

# Container Deployment using Docker

```
# build the container
docker build -t questionsui .

#run the container
docker run \
    -d \                          #run in daemonized mode
    --rm \                        #run in an ephemerial container; this does not make the volumes e.g data ephemerial
    -p 8000:8000 \                #expose the port
    -v ./data:/app/files \        #mount the directory for file uploads
    -v ./db:/app/db      \        #mount the directory for the database
    -e WEB_CONCURRENCY=$(nproc) \ #set the uvicorn processes
    questionsui
```

# ANL/Manual Development: 

```
# install spack if needed
git clone --depth=2 https://github.com/spack/spack.git
. spack/share/spack/setup-env.sh

# create new conda env
conda create -n labstyle python=3.12
conda activate labstyle

# use spack install npm and pip, and a few other dependencies
spack env activate .
spack install

# install frontend dependencies
cd frontend/
npm install

# alternatively "npm run builddev" for a development build
npm run build

#install backend dependencies
cd ../backend
pip install -r ./requirements.txt

#forward requests to the ai-backend running behind the ANL firewall
ssh -J $ANL_USER@login.cels.anl.gov -D 127.0.0.1:10106 $ANL_USER@agpt-questions-vmw-01.cels.anl.gov
export ALL_PROXY=socks5://127.0.0.1:10106

# run the backend that hosts the frontend (as a background process in bash)
pip install uvicorn[standard]
uvicorn --reload backend:app &

# run the frontend with hot-reloading, this will proxy requests to the backend
cd ../frontend
npm run dev
```

# ANL/Manual Deployment

To administer the site deployment, you'll need a CELS account and to be part of the group
`AuroraGPTQuestions` contact @robertu94 to be added.

There is a [Globus App entry](https://app.globus.org/settings/developers/projects/53651812-5228-4422-8067-cb01e3538a11/apps).  For access request through @robertu94

There is a mailing list `agptquestionsform@cels.lists.anl.gov` for support for
external users.  Contact @robertu94 to be added to this.

There is a slack channel `#agpt-questions-form` to discuss development on the
CELS slack, if you are member of CELS, you should be able to join it freely
otherwise request access from CELS support at `help@cles.anl.gov`.

For the question testing function to be work, the persistence inference must be
running.  For support for the persistent inference server ask in
`#agpt-deployment-inference-runtime-apis` in the CELS slack which is
responsible for managing it.

To access the site, you'll need to [ssh to the CELS GCE environment](https://help.cels.anl.gov/docs/linux/ssh/).

The deployment at ANL has a simple PHP based proxy server to relay requests to the backend hosted on GCE.  You can find the source for this `/nfs/pub_html/gce/projects/auroragptquestions/index.php` and the Apache access control file in  `/nfs/pub_html/gce/projects/auroragptquestions/.htaccess`

From there you can `ssh $USER@agpt-questions-vmw-01` to access the VM. The app itself is deployed in `/app`

The deployment is administered using a service account `agpt` without privileges.

You also have privileges to:

+ do anything as the service user `sudo -u agpt /bin/bash`
+ restart the server `sudo systemctl restart questionsui.service`
+ check the logs `sudo journalctl -u questionsui.service`
+ edit the systemd service file `sudoedit /etc/systemd/system/questionsui.service` for this sevice
+ edit any files in `/app`

If you need more permissions than this, Robert Underwood, Franck Cappello, and CELS support have administrative privileges.

All other requests need to go through CELS support `help@cels.anl.gov`.


# Debugging requests to the AI Backend

Requests are set over HTTPS to the globus compute backend, you can intercept these with a tool like wireshark.
To do that you'll need to set `SSLKEYLOGFILE` before starting the backend, and then configure wireshark preferences -> protocols -> tls -> master secret log file name to point to this file.

# Citing this tool

```bibtex
@article{Cappello_Madireddy_Underwood_Getty_Chia_Ramachandra_Nguyen_Keceli_Mallick_Li_et_al._2025,
    title={EAIRA: Establishing a Methodology for Evaluating AI Models as Scientific Research Assistants},
    url={http://arxiv.org/abs/2502.20309},
    DOI={10.48550/arXiv.2502.20309},
    note={arXiv:2502.20309 [cs]}, 
    number={arXiv:2502.20309}, 
    publisher={arXiv},
    author={Cappello, Franck and Madireddy, Sandeep and Underwood, Robert and Getty, Neil and Chia, Nicholas Lee-Ping and Ramachandra, Nesar and Nguyen, Josh and Keceli, Murat and Mallick, Tanwi and Li, Zilinghan and Ngom, Marieme and Zhang, Chenhui and Yanguas-Gil, Angel and Antoniuk, Evan and Kailkhura, Bhavya and Tian, Minyang and Du, Yufeng and Ting, Yuan-Sen and Wells, Azton and Nicolae, Bogdan and Maurya, Avinash and Rafique, M. Mustafa and Huerta, Eliu and Li, Bo and Foster, Ian and Stevens, Rick},
    year={2025},
    month=feb 
}
```

# Acknowledgements

We acknowledge the contributions code, methodology, and early testing/feedback of The AuroraGPT Evaluation Team including Franck Cappello, Sandeep Madireddy, Robert Underwood, Avinash Maurya, Zilinghan Li, Craig Stacy, Anthony Avarca, Neil Getty, Nicholas Lee-Ping Chia, Nesar Ramachandra, Josh Nguyen, Murat Keçeli, Tanwi Mallick, Chenhui Zhang, Angel Yanguas-Gil, Brad A. Ulrick, Minyang Tian, Azton Wells, Eliu Huerta, Ian Foster, Rick Stevens.

This material is based upon work supported by Laboratory Directed Research and Development (LDRD) funding from Argonne National Laboratory, provided by the Director, Office of Science, of the U.S. Department of Energy under Contract No. DE-AC02-06CH11357
