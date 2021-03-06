#!/usr/bin/python
import sys
import os
import subprocess

#===============================================================================================================
#BUILD YOUR OWN CMAKE.PY TO RUN CMAKE
# PATH TO LIBRARY:    os.environ['MAGMA'] ="/ccs/home/hshi/magma/magma-1.6.1"
# CHOOSE COMPILER:   -DCMAKE_CXX_COMPILER=mpic++
# ADD COMPILER FLAG: -DCMAKE_CXX_FLAGS='-Wall -O3'
# ADD DEFINATION:    -DCOMPILER_EXTRA_DEF:STRING='-DMPI_HAO'   //NEED TO USE -DMPI_HAO IF WE WANT MPI VERSION
# ADD MOUDLE PATH:   -DCMAKE_MODULE_PATH='~/Modules'           //DEFAULT IS ~/lib/Modules
# EXAMPLE:
#  os.environ['MAGMA'] ="/ccs/home/hshi/magma/magma-1.6.1"
#  com="cmake -DCMAKE_CXX_COMPILER=CC \
#             -DCMAKE_CXX_FLAGS='-Wall -O3 -fopenmp' \
#             -DCOMPILER_EXTRA_DEF:STRING='-DMPI_HAO' \
#             -DUSE_MAGMA=on \
#             -DCMAKE_MODULE_PATH='~/cmake/Modules' \
#             -DCMAKE_INSTALL_PREFIX:PATH="+install_dirc_name+" "+src_path
#===============================================================================================================

#Read from command line
typ  = sys.argv[1]
src_path = sys.argv[2]
if( len(sys.argv)<=3 ):
  install_dirc_name="~/lib/default"
else:
  install_dirc_name=sys.argv[3]

#Different types
if(typ=="mpi"):
  os.environ['LIBHAO']           = "~/lib/lib_hao/mpi1.0"
  os.environ['GHF_HUBBARD_FFTW'] = "~/lib/ghf_hubbard_fftw/mpi1.0"
  com="cmake -DCMAKE_CXX_COMPILER=mpic++ \
             -DCMAKE_CXX_FLAGS='-Wall -O3'\
             -DCOMPILER_EXTRA_DEF:STRING='-DMPI_HAO' \
             -DCMAKE_INSTALL_PREFIX:PATH="+install_dirc_name+" "+src_path
elif(typ=="serial"):
  os.environ['LIBHAO'] = "~/lib/lib_hao/serial1.0"
  os.environ['GHF_HUBBARD_FFTW'] = "~/lib/ghf_hubbard_fftw/serial1.0"
  com="cmake -DCMAKE_CXX_FLAGS='-Wall -O3' \
             -DCMAKE_INSTALL_PREFIX:PATH="+install_dirc_name+" "+src_path
elif(typ=="storm"):
  os.environ['LIBHAO'] = "~/lib/lib_hao/storm1.0"
  os.environ['SPRNG'] = "~/sprng2.0"
  os.environ['GHF_HUBBARD_FFTW'] = "~/lib/ghf_hubbard_fftw/storm1.0"
  com="cmake -DCMAKE_CXX_COMPILER=mpicxx \
             -DCMAKE_CXX_FLAGS='-Wall -O3' \
             -DCOMPILER_EXTRA_DEF:STRING='-DMPI_HAO' \
             -DCMAKE_INSTALL_PREFIX:PATH="+install_dirc_name+" "+src_path
elif(typ=="hu"):
  os.environ['LIBHAO'] = "~/lib/lib_hao/hu1.0"
  os.environ['SPRNG'] = "~/sprng2.0"
  os.environ['GHF_HUBBARD_FFTW'] = "~/lib/ghf_hubbard_fftw/hu1.0"
  com="cmake -DCMAKE_CXX_COMPILER=mpicxx \
             -DCMAKE_CXX_FLAGS='-Wall -O3 -march=corei7 -m64' \
             -DCOMPILER_EXTRA_DEF:STRING='-DMPI_HAO' \
             -DCMAKE_INSTALL_PREFIX:PATH="+install_dirc_name+" "+src_path
elif(typ=="humagma"):
  os.environ['LIBHAO'] = "~/lib/lib_hao/humagma1.0"
  os.environ['SPRNG'] = "~/sprng2.0"
  os.environ['GHF_HUBBARD_FFTW'] = "~/lib/ghf_hubbard_fftw/humagma1.0"
  com="cmake -DCMAKE_CXX_COMPILER=mpicxx \
             -DCMAKE_CXX_FLAGS='-Wall -O3 -march=corei7 -m64' \
             -DCOMPILER_EXTRA_DEF:STRING='-DMPI_HAO' \
             -DUSE_MAGMA=on \
             -DCMAKE_INSTALL_PREFIX:PATH="+install_dirc_name+" "+src_path
elif(typ=="comet"):
  os.environ['LIBHAO'] = "~/lib/lib_hao/comet1.0"
  os.environ['SPRNG'] = "~/sprng/sprng2.0"
  os.environ['GHF_HUBBARD_FFTW'] = "~/lib/ghf_hubbard_fftw/comet1.0"
  com="cmake -DCMAKE_CXX_COMPILER=mpicxx \
             -DCMAKE_CXX_FLAGS='-Wall -O3 -xHOST' \
             -DCOMPILER_EXTRA_DEF:STRING='-DMPI_HAO' \
             -DCMAKE_INSTALL_PREFIX:PATH="+install_dirc_name+" "+src_path
elif(typ=="titan"):
  os.environ['LIBHAO'] = "~/lib_hao/titan1.0"
  os.environ['SPRNG'] = os.environ['SPRNG_DIR']
  os.environ['FFTW']  = "/opt/fftw/3.3.4.0/interlagos"
  os.environ['ACML']  = "/opt/acml/5.3.1/gfortran64"
  com="cmake -DCMAKE_CXX_COMPILER=CC \
             -DCMAKE_CXX_FLAGS='-Wall -O3 -fopenmp' \
             -DCOMPILER_EXTRA_DEF:STRING='-DMPI_HAO' \
             -DCMAKE_MODULE_PATH='~/cmake/Modules' \
             -DCMAKE_INSTALL_PREFIX:PATH=~/lib_hao/mpi "+src_path

subprocess.call(com, shell=True )
