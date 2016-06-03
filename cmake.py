#!/usr/bin/python
import sys
import os
import subprocess

typ  = sys.argv[1]
src_path = sys.argv[2]
if( len(sys.argv)<=3 ):
  install_dirc_name="~/lib/default"
else:
  install_dirc_name=sys.argv[3]

if(typ=="mpi"):
  os.environ['LIBHAO']           = "~/lib/lib_hao/mpi"
  os.environ['GHF_HUBBARD_FFTW'] = "~/lib/ghf_hubbard_fftw/mpi"
  com="cmake -DCMAKE_CXX_COMPILER=mpic++ \
             -DCOMPILER_EXTRA_FLAG:STRING='-Wall -O3 -std=c++11' \
             -DCOMPILER_EXTRA_DEF:STRING='-DMPI_HAO' \
             -DMODULE_EXTRA_PATH:STRING='~/lib/Modules' \
             -DCMAKE_INSTALL_PREFIX:PATH="+install_dirc_name+" "+src_path
elif(typ=="serial"):
  os.environ['LIBHAO'] = "~/lib/lib_hao/serial"
  os.environ['GHF_HUBBARD_FFTW'] = "~/lib/ghf_hubbard_fftw/serial"
  com="cmake -DCOMPILER_EXTRA_FLAG:STRING='-Wall -O3 -std=c++11' \
             -DCOMPILER_EXTRA_DEF:STRING=' '\
             -DMODULE_EXTRA_PATH:STRING='~/lib/Modules' \
             -DCMAKE_INSTALL_PREFIX:PATH="+install_dirc_name+" "+src_path
elif(typ=="storm"):
  os.environ['LIBHAO'] = "~/lib/lib_hao/mpi"
  os.environ['SPRNG'] = "~/sprng2.0"
  com="cmake -DCMAKE_CXX_COMPILER=mpicxx \
             -DCOMPILER_EXTRA_FLAG:STRING='-Wall -O3 -std=c++11' \
             -DCOMPILER_EXTRA_DEF:STRING='-DMPI_HAO' \
             -DMODULE_EXTRA_PATH:STRING='~/lib/Modules' \
             -DCMAKE_INSTALL_PREFIX:PATH="+install_dirc_name+" "+src_path
elif(typ=="hu"):
  os.environ['LIBHAO'] = "~/lib_hao/mpi"
  os.environ['SPRNG'] = "~/sprng2.0"
  com="cmake -DCMAKE_CXX_COMPILER=mpicxx \
             -DCOMPILER_EXTRA_FLAG:STRING='-Wall -O3 -march=corei7 -m64 -std=c++11' \
             -DCOMPILER_EXTRA_DEF:STRING='-DMPI_HAO' \
             -DMODULE_EXTRA_PATH:STRING='~/cmake/Modules' \
             -DCMAKE_INSTALL_PREFIX:PATH=~/lib_hao/mpi "+src_path
elif(typ=="hu+magma"):
  os.environ['LIBHAO'] = "~/lib_hao/mpimagma"
  os.environ['SPRNG'] = "~/sprng2.0"
  com="cmake -DCMAKE_CXX_COMPILER=mpicxx \
             -DCOMPILER_EXTRA_FLAG:STRING='-Wall -O3 -march=corei7 -m64 -std=c++11' \
             -DCOMPILER_EXTRA_DEF:STRING='-DMPI_HAO' \
             -DUSE_MAGMA=on \
             -DMODULE_EXTRA_PATH:STRING='~/cmake/Modules' \
             -DCMAKE_INSTALL_PREFIX:PATH=~/lib_hao/mpimagma "+src_path
elif(typ=="titan"):
  os.environ['LIBHAO'] = "~/lib_hao/mpi"
  os.environ['SPRNG'] = os.environ['SPRNG_DIR']
  os.environ['FFTW']  = "/opt/fftw/3.3.4.0/interlagos"
  os.environ['ACML']  = "/opt/acml/5.3.1/gfortran64"
  com="cmake -DCMAKE_CXX_COMPILER=CC \
             -DCOMPILER_EXTRA_FLAG:STRING='-Wall -O3 -fopenmp -std=c++11' \
             -DCOMPILER_EXTRA_DEF:STRING='-DMPI_HAO' \
             -DMODULE_EXTRA_PATH:STRING='~/cmake/Modules' \
             -DCMAKE_INSTALL_PREFIX:PATH=~/lib_hao/mpi "+src_path
elif(typ=="titan+magma"):
  os.environ['LIBHAO'] = "~/lib_hao/mpimagma"
  os.environ['SPRNG'] = os.environ['SPRNG_DIR']
  os.environ['FFTW']  = "/opt/fftw/3.3.4.0/interlagos"
  os.environ['ACML']  = "/opt/acml/5.3.1/gfortran64"
  os.environ['MAGMA'] ="/ccs/home/hshi/magma/magma-1.6.1"
  com="cmake -DCMAKE_CXX_COMPILER=CC \
             -DCOMPILER_EXTRA_FLAG:STRING='-Wall -O3 -fopenmp -std=c++11' \
             -DCOMPILER_EXTRA_DEF:STRING='-DMPI_HAO' \
             -DUSE_MAGMA=on \
             -DMODULE_EXTRA_PATH:STRING='~/cmake/Modules' \
             -DCMAKE_INSTALL_PREFIX:PATH=~/lib_hao/mpimagma "+src_path

subprocess.call(com, shell=True )
